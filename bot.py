import logging
import json
import os

from flask_slack import Slack
from flask import Flask

slack_token = os.environ.get('SLACK_TOKEN', '')
slack_team_id = os.environ.get('SLACK_TEAM_ID', '')
logger = logging.getLogger('bot')

app = Flask(__name__)
slack = Slack(app)
app.add_url_rule('/slackbot', view_func=slack.dispatch)


@slack.command('my_search', token=slack_token,
               team_id=slack_team_id, methods=['POST'])
def my_search(**kwargs):
  _log_request(kwargs)
  text = kwargs.get('text')
  return slack.response('you are searching for : {0}'.format(text), response_type='in_channel')

def _log_request(request):
  request['token']='...'
  logger.info(msg='Slack Event: {0}'.format(json.dumps(request)))

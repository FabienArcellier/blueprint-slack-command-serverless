#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
from setuptools import setup, find_packages

setup(
  name='blueprint-slack-command-serverless',
  version='1.0',
  packages=find_packages(exclude=["*_tests"]),
  license='MIT',
  long_description=io.open('README.md').read(),
  classifier=[],
  install_requires=[
    'flask',
    'flask-slack',
    'zappa'
  ]
)

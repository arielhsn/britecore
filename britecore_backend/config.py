#!/usr/bin/env python

import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = 'iofrejiods'
DATABASE_URI = 'mysql+pymysql://britecoreuser:britecorepassword@localhost/britecore'
DATABASE_CONNECT_OPTIONS = {}

del os

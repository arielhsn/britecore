#!/usr/bin/env python

from flask import Flask

from britecore_backend.controllers import main

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(main.mod)

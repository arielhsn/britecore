#!/usr/bin/env python

from flask import Blueprint
from flask import request as flaskrequest
from flask_cors import CORS

from britecore_backend.models import client
from britecore_backend.models import product_area
from britecore_backend.models import request

mod = Blueprint('main', __name__)
CORS(mod)


@mod.route('/')
def index():
    return 'Engineering Project'


@mod.route('/client', methods=['GET'])
def getClient():
    return client.get_all()


@mod.route('/product_area', methods=['GET'])
def getProductArea():
    return product_area.get_all()


@mod.route('/request', methods=['GET'])
def getRequest():
    return request.get_all()


@mod.route('/request', methods=['POST'])
def postRequest():
    request.save(flaskrequest.get_json())
    return 'Ok'

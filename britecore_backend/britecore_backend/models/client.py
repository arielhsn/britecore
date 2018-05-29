#!/usr/bin/env python

from flask import jsonify

from database import db


class Client(db.Model):

    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(255), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'fullname': self.fullname
        }


def get_all():
    return jsonify(clients=[i.serialize for i in Client.query.order_by(Client.fullname).all()])

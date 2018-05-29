#!/usr/bin/env python

from flask import jsonify

from database import db


class ProductArea(db.Model):

    __tablename__ = 'product_area'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


def get_all():
    return jsonify(product_areas=[i.serialize for i in ProductArea.query.order_by(ProductArea.name).all()])

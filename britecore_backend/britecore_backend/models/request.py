#!/usr/bin/env python

from flask import jsonify

from database import db


class Request(db.Model):

    __tablename__ = 'request'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    client = db.relationship('britecore_backend.models.client.Client', foreign_keys=client_id)
    client_priority = db.Column(db.Integer, nullable=False)
    target_date = db.Column(db.Date, nullable=False)
    product_area_id = db.Column(db.Integer, db.ForeignKey('product_area.id'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'client_id': self.client_id,
            'client': self.client.serialize,
            'client_priority': self.client_priority,
            'target_date': self.target_date.isoformat(),
            'product_area_id': self.product_area_id
        }


def get_all():
    return jsonify(requests=[i.serialize for i in Request.query.order_by(Request.client_priority).all()])


def save(data):
    entity = Request()

    if 'id' in data:
        entity.client_id = data['id']

    entity.client_id = data['client_id']
    entity.client_priority = data['client_priority']
    entity.description = data['description']
    entity.product_area_id = data['product_area_id']
    entity.target_date = data['target_date']
    entity.title = data['title']

    requests = Request.query\
        .filter(Request.client_priority >= entity.client_priority)\
        .order_by(Request.client_priority)\
        .all()

    db.session.add(entity)

    if requests and len(requests) > 1:
        curr_priority = int(entity.client_priority)

        for i in range(0, len(requests)):
            request = requests[i]

            if curr_priority == request.client_priority:
                curr_priority += 1
                request.client_priority = curr_priority
                db.session.add(request)

    db.session.commit()

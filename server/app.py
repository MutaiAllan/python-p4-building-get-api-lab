#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from sqlalchemy import desc

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    all_bakeries = []
    for bakery in BakedGood.query.all():
        bakery_dict = {
            "bakery_id": bakery.bakery_id,
            "created_at": bakery.created_at,
            "id": bakery.id,
            "name": bakery.name,
            "price": bakery.price,
            "updated_at": bakery.updated_at
        }
        all_bakeries.append(bakery_dict)

    response = make_response(jsonify(all_bakeries), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    '''bakeryobj = BakedGood.query.filter_by(bakery_id=id).all()
    bakery_dict = [bakery.to_dict() for bakery in bakeryobj]
    response = make_response(jsonify(bakery_dict), 200)

    response.headers["Content-Type"] = "application/json"

    return response'''

    '''all_bakeries = []
    for bakery in BakedGood.query.filter_by(bakery_id=id).all():
        bakery_dict = {
            "bakery_id": bakery.bakery_id,
            "created_at": bakery.created_at,
            "id": bakery.id,
            "name": bakery.name,
            "price": bakery.price,
            "updated_at": bakery.updated_at
        }
        all_bakeries.append(bakery_dict)

    response_body = { "baked_goods": all_bakeries}
    response = make_response(jsonify(response_body), 200)
    response.headers["Content-Type"] = "application/json"
    return response'''
    bakeryobj = BakedGood.query.filter_by(bakery_id=id).all()

    baked_goods_list = []
    for baked_good in bakeryobj:
        baked_goods_dict = {
            "bakery_id": baked_good.bakery.id,
            "created_at": baked_good.created_at,
            "id": baked_good.id,
            "name": baked_good.name,
            "price": baked_good.price,
            "updated_at": baked_good.updated_at
        }
        baked_goods_list.append(baked_goods_dict)

    bakery_dict = {
        "baked_goods": baked_goods_list,
        "created_at": "2022-09-12 21:01:00",
        "id": 2,
        "name": "Cook-Cunningham",
        "updated_at": None
    }

    response = make_response(jsonify(bakery_dict), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    all_bakeries = []
    for bakery in BakedGood.query.order_by(BakedGood.price.desc()).all():
        bakery_dict = {
            "bakery_id": bakery.bakery_id,
            "created_at": bakery.created_at,
            "id": bakery.id,
            "name": bakery.name,
            "price": bakery.price,
            "updated_at": bakery.updated_at
        }
        all_bakeries.append(bakery_dict)

    response = make_response(jsonify(all_bakeries), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    '''most_expensive = BakedGood.query.order_by(BakedGood.price.desc()).limit(1)
    bakery = Bakery.query.filter_by(id=most_expensive.bakery_id).first()
    bakery_dict = {
        "created_at": bakery.created_at,
        "id": bakery.id,
        "name": bakery.name,
        "updated_at": bakery.updated_at
    }
    bakery_good = {
        "bakery": bakery_dict,
        "created_at": most_expensive.created_at,
        "id": most_expensive.id,
        "name": most_expensive.name,
        "price": most_expensive.price,
        "updated_at": most_expensive.updated_at
    }
    response = make_response(bakery_good, 200)
    return response'''
    '''all_bakeries = []
    for bakery in BakedGood.query.order_by(BakedGood.price.desc()).limit(1):
        bakery_dict = {
            "bakery_id": bakery.bakery_id,
            "created_at": bakery.created_at,
            "id": bakery.id,
            "name": bakery.name,
            "price": bakery.price,
            "updated_at": bakery.updated_at
        }
        all_bakeries.append(bakery_dict)

    response = make_response(jsonify(all_bakeries), 200)
    response.headers["Content-Type"] = "application/json"
    return response'''
    most_expensive = BakedGood.query.order_by(desc(BakedGood.price)).first()

    bakery_dict = {
        "bakery_id": most_expensive.bakery_id,
        "created_at": most_expensive.created_at,
        "id": most_expensive.id,
        "name": most_expensive.name,
        "price": most_expensive.price,
        "updated_at": most_expensive.updated_at
    }
    response = make_response(jsonify(bakery_dict), 200)
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)

from flask import Flask, Blueprint
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

api = Api(app)

items = []


class Item(Resource):
    def get(self, name: str):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item is not None else 404

    def post(self, name: str):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
            type=float,
            required=True,
            help="This field cannot be left blank!"
        )
        data = parser.parse_args()
        for item in items:
            if item['name'] == name:
                return {'message':"An item with name '{}' already exist!".format(name)}, 400
        item = {'name': name.capitalize(), 'price': data['price']}
        items.append(item)
        return item, 201
    
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': "'{}' deleted.".format(name)}
    
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
            type=float,
            required=True,
            help="This field cannot be left blank!"
        )
        data = parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name':name,'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items},200


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=3333, debug=True)

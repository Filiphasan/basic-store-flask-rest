from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My First Store Obj',
        'items': [
            {
                'name': 'First Item',
                'price': 14.99
            }
        ]
    }
]

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'data': stores})

#POST /store
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store),201

# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'error','store not found'})

# GET /store/<string:name>/item
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'error','store not found'})


app.run(port=3333)

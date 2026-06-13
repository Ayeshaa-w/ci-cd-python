from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# In-memory store (stateless per restart — intentional)
items = {}
counter = {"id": 1}

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'name field required'}), 400
    item_id = counter["id"]
    items[item_id] = {"id": item_id, "name": data["name"]}
    counter["id"] += 1
    app.logger.info(f"Created item {item_id}")
    return jsonify(items[item_id]), 201

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(list(items.values())), 200

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({'error': 'not found'}), 404
    return jsonify(item), 200

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({'error': 'not found'}), 404
    del items[item_id]
    app.logger.info(f"Deleted item {item_id}")
    return jsonify({'deleted': item_id}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
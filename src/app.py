from flask import Flask, request, jsonify
import os
from memory import MemoryStore
from item import Item
from receipt import Receipt
from models import ReceiptRequest

app = Flask(__name__)
memory_store = MemoryStore()

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    if not request.json:
        return jsonify({'error': 'No data provided'}), 400
    
    try:
        receipt_data = ReceiptRequest(**request.json)
        receipt = Receipt(
            receipt_data.retailer,
            receipt_data.purchaseDate,
            receipt_data.purchaseTime,
            [Item(item.shortDescription, item.price) for item in receipt_data.items],
            receipt_data.total
        )
        memory_store.receipts[receipt.get_receipt_id()] = receipt
        return jsonify({'id': receipt.get_receipt_id()})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/receipts/<id>/points', methods=['GET'])
def get_receipt_points(id: str):
    receipt = memory_store.receipts.get(id)
    if not receipt:
        return jsonify({'error': 'Receipt not found'}), 404
    return jsonify({'points': receipt.calculate_points()})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
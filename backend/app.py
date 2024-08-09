from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

@app.route('/')
def home():
    return "This is my Flask backend"

@app.route('/price', methods=['GET'])
def estimatePrice():
    mileage = request.args.get('mileage', type=int)
    price = 20000 - (mileage * 0.05)
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)

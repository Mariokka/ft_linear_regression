from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "This is my Flask backend"

@app.route('/predict', methods=['GET'])
def estimatePrice():
    mileage = request.args.get('mileage', type=int)
    price = 20000 - (mileage * 0.05)
    return jsonify({'predicted_price': price})

if __name__ == '__main__':
    app.run(debug=True)

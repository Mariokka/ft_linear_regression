from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

DEFAULT_THETA0 = 0
DEFAULT_THETA1 = 0
DEFAULT_MEAN_MILEAGE = 0
DEFAULT_STD_MILEAGE = 1

def initializeValues():
    if os.path.exists('../../model/result.txt'):
        with open('../../model/result.txt', 'r') as file:
            lines = file.readlines()
            theta0 = float(lines[0].strip())
            theta1 = float(lines[1].strip())
            mean_mileage = float(lines[2].strip())
            std_mileage = float(lines[3].strip())
        return theta0, theta1, mean_mileage, std_mileage
    else:
        return DEFAULT_THETA0, DEFAULT_THETA1, DEFAULT_MEAN_MILEAGE, DEFAULT_STD_MILEAGE

theta0, theta1, mean_mileage, std_mileage = initializeValues()

@app.route('/price', methods=['GET'])
def estimatePrice():
    mileage = request.args.get('mileage', type=int)
    normalized_mileage = (mileage - mean_mileage) / std_mileage
    price = theta0 + theta1 * normalized_mileage
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(port=5000, debug=True)

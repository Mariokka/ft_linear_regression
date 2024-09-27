from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

data = pd.read_csv('data.csv')
mileages = data['km'].values
prices = data['price'].values

theta0 = 0
theta1 = 0
learning_rate = 0.01
numberOfIterations = 1000

numberOfObservations = len(mileages)
mean_mileage = np.mean(mileages)
std_mileage = np.std(mileages)
normalized_mileages = (mileages - mean_mileage) / std_mileage

for _ in range(numberOfIterations):
    predictedPrices = theta0 + theta1 * normalized_mileages

    temp_theta0 = learning_rate * (1/numberOfObservations) * np.sum(predictedPrices - prices)
    temp_theta1 = learning_rate * (1/numberOfObservations) * np.sum((predictedPrices - prices) * normalized_mileages)

    theta0 = theta0 - temp_theta0
    theta1 = theta1 - temp_theta1

#     if _ % 100 == 0:
#         cost = (1/(2*numberOfObservations)) * np.sum((predictedPrices - prices) ** 2)
#         print(f"Iteration {_}: Cost {cost}, theta0 {theta0}, theta1 {theta1}")

@app.route('/')
def home():
    return "This is my Flask backend"

@app.route('/price', methods=['GET'])
def estimatePrice():
    mileage = request.args.get('mileage', type=int)
    price = theta0 + (theta1 * (mileage - mean_mileage) / std_mileage)
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)

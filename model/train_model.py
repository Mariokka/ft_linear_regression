from flask import Flask, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

data = pd.read_csv('data.csv')
mileages = data['km'].values
prices = data['price'].values

learning_rate = 0.01
numberOfIterations = 1000

numberOfObservations = len(mileages)
mean_mileage = np.mean(mileages)
std_mileage = np.std(mileages)
normalized_mileages = (mileages - mean_mileage) / std_mileage

def train_model():
    theta0, theta1 = calculate_thetas()

    with open('result.txt', 'w') as file:
        file.write(f"{theta0}\n{theta1}\n{mean_mileage}\n{std_mileage}\n")

def calculate_thetas():
    theta0 = 0
    theta1 = 0

    for _ in range(numberOfIterations):
        predictedPrices = theta0 + theta1 * normalized_mileages

        temp_theta0 = learning_rate * (1/numberOfObservations) * np.sum(predictedPrices - prices)
        temp_theta1 = learning_rate * (1/numberOfObservations) * np.sum((predictedPrices - prices) * normalized_mileages)

        theta0 = theta0 - temp_theta0
        theta1 = theta1 - temp_theta1

    return theta0, theta1

train_model()
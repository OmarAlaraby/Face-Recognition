import random
import numpy as np

class Adaline:
    def __init__(self, num_inputs, learning_rate=0.01, iterations=100):
        self.num_inputs = num_inputs
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.bias = 1
        self.errors = []
        self.init_weights()
        self.classification_rate = []

    def activate(self, input) -> int:
        if input >= 0:
            return 1
        return -1

    def init_weights(self):
        self.weights = np.array([random.random() for _ in range(self.num_inputs)])

    def multiply(self, inputs) -> float:
        output = 0
        for i in range(len(inputs)):
            output += inputs[i] * self.weights[i]
        return output

    def calculate_MSE(self, Y_hat, Y) -> float:
        MSE = ((Y - Y_hat) ** 2).sum() / len(Y)
        return MSE

    def calculate_classification_rate(self, Y_hat, Y) -> float:
        return np.mean(Y_hat == Y)

    def update_weights(self, X, Y_hat, Y) -> None:
        errors = 2 * (Y - Y_hat)
        self.weights[:] += self.learning_rate * X.T.dot(errors)
        self.bias += self.learning_rate * errors.sum()

    def train(self, X, Y):
        for _ in range(self.iterations):
            Y_hat = np.array([])
            for i in range(len(X)):
                Y_hat = np.append(Y_hat, self.activate(self.multiply(X[i]) + self.bias))
            print(_)
            self.update_weights(X, Y_hat, Y)
            MSE = self.calculate_MSE(Y_hat, Y)
            self.errors.append(MSE)
            self.classification_rate.append(self.calculate_classification_rate(Y_hat, Y) * 100)

    def predict(self, X):
        prediction = self.activate(self.multiply(X) + self.bias)
        return 'Apple' if prediction == 1 else 'Banana'

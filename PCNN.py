'''
i spend 5 days implementing this PCNN class, if you try to fix it.
please count the number of hours you waste here

number of hours wasted here = 30
'''
import cv2
import numpy as np
import json
from scipy.special import expit
from sklearn.utils import class_weight
from imblearn.over_sampling import RandomOverSampler

class PCNN_Model:
    def __init__(self, input_size, num_neurons, alpha=0.001, beta=0.0000001):
        self.weights = np.random.rand(num_neurons, input_size)  # el weights will be updated in the training process
        self.threshold = np.ones(num_neurons)
        self.alpha = alpha
        self.beta = beta
        self.bananasDataPath = 'Data/bananas.json'
        self.applesDataPath = 'Data/apples.json'
        self.startTraining()

    def extract_features(self, img):
        try:
            img = cv2.resize(img, (32, 32))
            num_channels = img.shape[2]
            if num_channels == 3:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            features = img.flatten() / 255.0
            return features

        except Exception as e:
            print(f"Error extracting features from image: {e}")
            return None

    def preProcess(self, image):
        if type(image) != str :
            return False
        return self.extract_features(cv2.imread(image))

    def load_data(self):
        with open(self.applesDataPath, 'r') as f:
            apples_data = json.load(f)

        with open(self.bananasDataPath, 'r') as f:
            bananas_data = json.load(f)

        images = []
        labels = []
        for item in apples_data:
            images.append(item["path"])
            labels.append(1)

        for item in bananas_data:
            images.append(item["path"])
            labels.append(0)

        print(images)

        preprocessed_images = []
        for image_path in images:
            image = self.preProcess(image_path)
            if type(image) != bool:
                preprocessed_images.append(image)

        return np.array(preprocessed_images), np.array(labels)

    def startTraining(self):
        images, labels = self.load_data()
        epochs = 20  # Adjust epochs as needed
        self.train(images, labels, epochs)

    def train(self, images, labels, epochs):
        for epoch in range(epochs):
            for image, label in zip(images, labels):
                local_activity = self.calculate_local_activity(image)

                winning_neuron = np.argmax(local_activity)
                self.update_threshold(winning_neuron, local_activity)

                self.weights *= 1 - self.alpha

    def calculate_local_activity(self, image):
        features = self.weights * image
        return np.sum(features, axis=1)

    def update_threshold(self, winning_neuron, local_activity):
        self.threshold -= self.beta * self.threshold
        self.threshold[winning_neuron] = max(self.threshold[winning_neuron], local_activity[winning_neuron])

    def predict(self, image):
        image = self.preProcess(image)
        local_activity = self.calculate_local_activity(image)
        output = expit(local_activity - self.threshold)
        predicted_class = np.argmax(output)

        class_labels = {0: "Banana", 1: "Apple"}
        if predicted_class > 1 :
            predicted_class = 0
        return class_labels[predicted_class]

    def check_accuracy(self):
        images , labels = self.load_data()
        predictions = [self.predict(img) for img in images]
        correct = sum(pred == label for pred, label in zip(predictions, labels))
        accuracy = correct / len(labels) * 100
        return accuracy


def main():

    pcnn = PCNN_Model(1024, 2, alpha=0.05, beta=0.001)
    print(pcnn.check_accuracy())

    image = 'Images/bananas/banana.jpg'
    prediction = pcnn.predict(image)
    print(prediction)

if __name__ == "__main__":
  main()

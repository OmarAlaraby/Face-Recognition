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
        self.threshold = np.ones(num_neurons)  # initially [1, 1, 1, .... 1]
        self.alpha = alpha  # learning rate for linking layer weights
        self.beta = beta  # learning rate for thresholds
        self.menDataPath = 'Data/men.json'
        self.womenDataPath = 'Data/women.json'
        self.vgg_model = None  # Removed VGG16 features
        self.startTraining()  # Call training on initialization (optional)

    def extract_features(self, cv2_img):
        # Preprocessing without VGG16 features
        img = cv2.resize(cv2_img, (32, 64))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = img.flatten() / 255  # To be normalized
        return img

    def preProcess(self, image):
        return self.extract_features(image)  # Use the new extract_features

    def load_data(self):
        with open(self.menDataPath, 'r') as f:
            men_data = json.load(f)

        with open(self.womenDataPath, 'r') as f:
            women_data = json.load(f)

        images = []
        labels = []
        for item in men_data:
            images.append(item["path"])
            labels.append(1)  # Assuming "1" represents male

        for item in women_data:
            images.append(item["path"])
            labels.append(0)  # Assuming "0" represents female
        print(images)
        print(labels)

        # Define class weights based on your data (assuming "0" is female, "1" is male)
        class_weights = {'0': 2.48042705, '1': 0.6262354}

        # Oversample using class weights for balanced sampling
        oversample = RandomOverSampler(sampling_strategy=class_weights)
        images_resampled, labels_resampled = oversample.fit_resample(np.array(images)[:, np.newaxis], labels)

        preprocessed_images = []
        for image_path in images_resampled:
            image = self.preProcess(cv2.imread(image_path[0]))
            preprocessed_images.append(image)

        return np.array(preprocessed_images), np.array(labels_resampled)

    def startTraining(self):
        images, labels = self.load_data()
        epochs = 20  # Adjust epochs as needed
        self.train(images, labels, epochs)

    def train(self, images, labels, epochs):
        for epoch in range(epochs):
            for image, label in zip(images, labels):
                local_activity = self.calculate_local_activity(image)

                winning_neuron = np.argmax(local_activity)  # get the index of the maximum value
                self.update_threshold(winning_neuron, local_activity)

                # Linking layer weight decay
                self.weights *= 1 - self.alpha

    def calculate_local_activity(self, image):
        # No need to reshape the image here
        features = self.weights * image
        return np.sum(features, axis=1)

    def update_threshold(self, winning_neuron, local_activity):
        self.threshold -= self.beta * self.threshold
        self.threshold[winning_neuron] = max(self.threshold[winning_neuron], local_activity[winning_neuron])

    def predict(self, image):
        image = self.preProcess(image)
        local_activity = self.calculate_local_activity(image)
        output = expit(local_activity - self.threshold)
        predicted_class = np.argmax(output)  # Get the index of the class with highest probability

        # Map predicted class index to gender label (optional)
        class_labels = {0: "female", 1: "male"}  # adjust based on your label assignment
        return class_labels[predicted_class]

    def check_accuracy(self, images, labels):
        predictions = [self.predict(img) for img in images]
        correct = sum(pred == label for pred, label in zip(predictions, labels))
        accuracy = correct / len(labels) * 100  # Calculate accuracy percentage
        return accuracy


def main():
    image = cv2.imread('Images/Women/297883_1952-01-14_2008.jpg')

    pcnn = PCNN_Model(2048, 150, alpha=0.05, beta=0.001)
    print(pcnn.check_accuracy())

    # Prediction
    prediction = pcnn.predict(image)
    class_labels = ["Female", "Male"]

    if 1 < prediction or prediction < 0:
        print(prediction)
        print("Detection failed")
    else :
        print(f"Predicted Class: {class_labels[prediction]}")

if __name__ == "__main__":
  main()

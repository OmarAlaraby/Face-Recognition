import numpy as np

class HebbianLearning:
    def __init__(self):
        self.data_set = []
        self.labels = []
        self.weights = np.array([])
        self.bias = np.array([])
        self.image = None

    def flatten_img(self, img):
        return np.array(img).flatten()

    def is_error(self):
        pass

    def train(self):
        pass

    def add_data(self):
        pass

    def predict(self) :
        pass

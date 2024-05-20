import numpy as np
import json
from PIL import Image

def preProcess(image):
    return np.array(image).flatten()

def load_data():
    applesDataPath = 'Data/apples.json'
    bananasDataPath = 'Data/bananas.json'
    with open(applesDataPath, 'r') as f:
        apples_data = json.load(f)

    with open(bananasDataPath, 'r') as f:
        bananas_data = json.load(f)

    images = []
    labels = []
    for item in apples_data:
        image = Image.open(item["path"])
        image = image.resize((200, 200))
        images.append(preProcess(image))
        labels.append(1)

    for item in bananas_data:
        image = Image.open(item["path"])
        image = image.resize((200, 200))
        images.append(preProcess(image))
        labels.append(0)

    return np.array(images), np.array(labels)

def fix(input) :
    return 1 if input >= 0 else -1
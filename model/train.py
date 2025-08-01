# ===== train.py =====
# Treina o modelo com base nas imagens
import os
import numpy as np
import cv2
import tensorflow as tf
from sklearn.preprocessing import LabelBinarizer
from config import characters, captcha_length, image_height, image_width
from model import build_model

lb = LabelBinarizer()
lb.fit(characters)

def load_data(data_dir):
    X = []
    Y = [[] for _ in range(captcha_length)]

    for file in os.listdir(data_dir):
        label = file.split('.')[0]
        img = cv2.imread(os.path.join(data_dir, file), cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (image_width, image_height))
        img = img / 255.0
        X.append(img.reshape((image_height, image_width, 1)))
        for i, char in enumerate(label):
            Y[i].append(lb.transform([char])[0])

    X = np.array(X)
    Y = [np.array(y) for y in Y]
    return X, Y

X, Y = load_data('data/train')
model = build_model()
model.fit(X, Y, epochs=30, batch_size=16)
model.save('captcha_model.h5')

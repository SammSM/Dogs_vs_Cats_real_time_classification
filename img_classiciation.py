import numpy as np
import cv2
import keras
from keras.models import load_model
import pickle

model = load_model('dogs_vs_cats_h5.h5')

def pred_img(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (128, 128))
    img = img.reshape(1, 128, 128, 1)
    img = img/255

    prediction = model.predict(img)
    
    if prediction > 0.7:
        return 'Dog'
    elif prediction < 0.3:
        return 'Cat'
    else:
        return 'Not detected'
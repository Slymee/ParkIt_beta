import numpy as np
import cv2 as cv
import tensorflow as tf


from tensorflow import keras
from keras import layers
from keras.layers import Dense


def load_dataset(dataset_dir):
    # Load the images and labels
    images = []
    labels = []
    with open(dataset_dir + '/labels.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(' ')
            image_file = dataset_dir + '/' + parts[0]
            label = [float(p) for p in parts[1:]]
            image = cv.imread(image_file, cv.IMREAD_GRAYSCALE)
            images.append(image)
            labels.append(label)
    # Convert the images and labels to NumPy arrays
    images = np.array(images)
    labels = np.array(labels)
    # Normalize the pixel values to [0, 1]
    images = images.astype('float32') / 255.
    # Reshape the images to (n_samples, width, height, n_channels)
    images = np.reshape(
        images, (images.shape[0], images.shape[1], images.shape[2], 1))
    return images, labels


# Training Module
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),  # neurons
    layers.Dense(10)
])

# Compiling Model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(
                  from_logits=True),
              metrics=['accuracy'])


# Train Model
model.fit([], [], epochs=10,
          validation_data=([], []))

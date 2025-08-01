# ===== model.py =====
# Define a arquitetura do modelo
import tensorflow as tf
from config import image_height, image_width, captcha_length, num_classes

def build_model():
    input_tensor = tf.keras.layers.Input(shape=(image_height, image_width, 1))
    x = tf.keras.layers.Conv2D(32, (3, 3), activation='relu')(input_tensor)
    x = tf.keras.layers.MaxPooling2D((2, 2))(x)
    x = tf.keras.layers.Conv2D(64, (3, 3), activation='relu')(x)
    x = tf.keras.layers.MaxPooling2D((2, 2))(x)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(1024, activation='relu')(x)
    x = tf.keras.layers.Dropout(0.5)(x)

    outputs = [
        tf.keras.layers.Dense(num_classes, activation='softmax', name=f'char_{i}')(x)
        for i in range(captcha_length)
    ]

    model = tf.keras.models.Model(inputs=input_tensor, outputs=outputs)
    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )
    return model
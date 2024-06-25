import os
from dotenv import load_dotenv
import numpy as np
from keras.models import model_from_json
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten, Input
from tensorflow.keras.optimizers import Adam
from keras.src.legacy.preprocessing.image import ImageDataGenerator
import tensorflow as tf

load_dotenv()
test = os.getenv('DATA_TEST_PATH')
train = os.getenv('DATA_TRAIN_PATH')
classes = int(os.getenv('CLASSES'))

train_data_gen = ImageDataGenerator(rescale=1./255)
validation_data_gen = ImageDataGenerator(rescale=1./255)

train_generator = train_data_gen.flow_from_directory(
    train,
    target_size=(48, 48),
    batch_size=16,
    color_mode="grayscale",
    class_mode="categorical"
)

validation_generator = validation_data_gen.flow_from_directory(
    test,
    target_size=(48, 48),
    batch_size=16,
    color_mode="grayscale",
    class_mode="categorical"
)

train_dataset = tf.data.Dataset.from_generator(
    lambda: train_generator,
    output_signature=(
        tf.TensorSpec(shape=(None, 48, 48, 1), dtype=tf.float32),
        tf.TensorSpec(shape=(None, classes), dtype=tf.float32)
    )
).repeat()

validation_dataset = tf.data.Dataset.from_generator(
    lambda: validation_generator,
    output_signature=(
        tf.TensorSpec(shape=(None, 48, 48, 1), dtype=tf.float32),
        tf.TensorSpec(shape=(None, classes), dtype=tf.float32)
    )
).repeat()


number_model = Sequential([
    Input(shape=(48, 48, 1)),
    Conv2D(32, kernel_size=(3, 3), activation='relu'),
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.25),
    Conv2D(128, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(128, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.25),
    Flatten(),
    Dense(1024, activation='relu'),
    Dropout(0.25),
    Dense(classes, activation='softmax')
])

steps_per_epoch = train_generator.samples // train_generator.batch_size
validation_steps = validation_generator.samples // validation_generator.batch_size

number_model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.0001), metrics=['accuracy'])

numbers_model_info = number_model.fit(
    train_dataset,
    steps_per_epoch=steps_per_epoch,
    epochs=50,
    validation_data=validation_dataset,
    validation_steps=validation_steps
)

model_json = number_model.to_json()
with open("models_number/number_model.json", "w") as json_file:
    json_file.write(model_json)

number_model.save_weights('models_number/number_model.weights.h5')
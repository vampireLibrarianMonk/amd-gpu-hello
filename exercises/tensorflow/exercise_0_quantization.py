import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Define a simple model
model = Sequential([
    Dense(units=1, input_shape=[1], activation='linear')
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Create some dummy data for training
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# Train the model
model.fit(xs, ys, epochs=100, verbose=0)

# Evaluate the model
print("Model trained.")

# Convert the model to the TensorFlow Lite format with quantization
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Generate a quantized model
tflite_model = converter.convert()

# Save the quantized model to a file
with open('quantized_model.tflite', 'wb') as f:
    f.write(tflite_model)

print("Quantized model saved.")
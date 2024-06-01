import tensorflow as tf
import numpy as np
import pandas as pd
import os

def testNeuralNetworkImplementationwithTwoInputVariable():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(script_dir, 'diabetes.csv')
    data = pd.read_csv(csv_file_path)
    X = data[['Glucose','BMI']]
    y = data[['Outcome']]

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(units=1, input_shape=(2,), activation='sigmoid')
    ])

    model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, y, epochs=10, verbose=1)

    print("Testing the perceptron:")
    predictions = model.predict(X)
    predictions = pd.Series(predictions.reshape(-1,1))
    result = pd.concat([X,y, predictions])
    print(result)

testNeuralNetworkImplementationwithTwoInputVariable()
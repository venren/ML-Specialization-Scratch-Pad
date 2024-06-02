import tensorflow as tf
import numpy as np
import pandas as pd
import os
import Network


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_dir, 'diabetes.csv')
data = pd.read_csv(csv_file_path)
X = data[['Glucose','BMI']]
y = data[['Outcome']]

def testNNWithTensorflow():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(units=1, input_shape=(2,), activation='sigmoid')
    ])

    model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, y, epochs=10, verbose=1)

    print("Testing the perceptron:")
    predictions = model.predict(X)
    predictions = pd.Series(predictions.flatten())
    X = X.reset_index(drop=True)
    y = y.reset_index(drop=True)
    predictions = predictions.reset_index(drop=True)
    predictions = predictions.apply(lambda x: 1 if x >= 0.5 else 0)
    result = pd.concat([X,y, predictions], axis=1)
    correct_predictions = (result['Outcome'] == result[0]).sum()
    total_predictions = len(predictions)
    accuracy = correct_predictions / total_predictions
    print("Accuracy:", accuracy)

def testNNPythonImplementation():
    network = Network.Network(20, X, y, np.array([2,3,1]))
    result = network.forwardProp()
    print("I am here!!!")


testNNPythonImplementation()    

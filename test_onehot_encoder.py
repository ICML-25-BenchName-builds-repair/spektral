import numpy as np
from sklearn.preprocessing import OneHotEncoder

# Test the OneHotEncoder with sparse=False parameter
try:
    encoder = OneHotEncoder(sparse=False, categories="auto")
    print("Using sparse=False works")
except TypeError as e:
    print(f"Error: {e}")

# Test the OneHotEncoder with sparse_output=False parameter
try:
    encoder = OneHotEncoder(sparse_output=False, categories="auto")
    print("Using sparse_output=False works")
except TypeError as e:
    print(f"Error: {e}")

# Test the encoder with some data
try:
    data = np.array([[0], [1], [2]])
    encoder = OneHotEncoder(sparse_output=False, categories="auto")
    result = encoder.fit_transform(data)
    print("Transformation successful")
    print(result)
except Exception as e:
    print(f"Error during transformation: {e}")
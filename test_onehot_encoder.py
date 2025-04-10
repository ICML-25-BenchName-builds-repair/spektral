"""
Test script to verify the OneHotEncoder issue and fix.
"""
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Test with the current parameter name (sparse_output)
print("Testing with sparse_output parameter:")
try:
    encoder = OneHotEncoder(sparse_output=False, categories="auto")
    result = encoder.fit_transform(np.array([[0], [1], [2]]))
    print("Success! Result shape:", result.shape)
except Exception as e:
    print("Error:", e)

# Test with the old parameter name (sparse)
print("\nTesting with sparse parameter:")
try:
    encoder = OneHotEncoder(sparse=False, categories="auto")
    result = encoder.fit_transform(np.array([[0], [1], [2]]))
    print("Success! Result shape:", result.shape)
except Exception as e:
    print("Error:", e)
import numpy as np

# Step 1: Training Data
# X = [videos watched, time spent]
# y = complete course (1) or drop out (0)

X = np.array([
    [2, 15],
    [3, 20],
    [8, 60],
    [9, 75]
])

y = np.array([[0], [0], [1], [1]])

# Step 2: Initialize weights and bias
np.random.seed(42)

input_size = 2
hidden_size = 3
output_size = 1

W1 = np.random.rand(input_size, hidden_size)
b1 = np.random.rand(hidden_size)

W2 = np.random.rand(hidden_size, output_size)
b2 = np.random.rand(output_size)

learning_rate = 0.01

# Step 3: Activation Function (Sigmoid)
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Derivative of sigmoid
def sigmoid_derivative(a):
    return a * (1 - a)

# Step 4: Training Loop
for epoch in range(1000):

    # Forward propagation
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2) + b2
    y_pred = sigmoid(final_input)

    # Error
    error = y - y_pred

    # Backpropagation
    d_output = error * sigmoid_derivative(y_pred)

    hidden_error = d_output.dot(W2.T)
    d_hidden = hidden_error * sigmoid_derivative(hidden_output)

    # Update weights
    W2 += learning_rate * hidden_output.T.dot(d_output)
    b2 += learning_rate * np.sum(d_output, axis=0)

    W1 += learning_rate * X.T.dot(d_hidden)
    b1 += learning_rate * np.sum(d_hidden, axis=0)

# Step 5: Testing the Neural Network
test_students = np.array([
    [4, 25],
    [10, 80]
])

hidden = sigmoid(np.dot(test_students, W1) + b1)
output = sigmoid(np.dot(hidden, W2) + b2)

print("Predictions (Probability of Completion):")
print(output)

print("\nClassification:")
print((output >= 0.5).astype(int))
import numpy as np

class NeuralNetwork(object):
   def __init__(self, size_input, size_hidden, size_output):
       self.W1 = np.random.randn(size_input, size_hidden)
       self.W2 = np.random.randn(size_hidden, size_output)

def sigmoid(z):
   return 1 / (1 + np.exp(-z))

def cost(y, y_hat):
    # 0.5 * (diff between desired output and generated output)^2
    return np.sum(0.5 * (y - y_hat) ** 2)

def main():

    # Input data
    X = np.array( ([3,5],[5,1],[10,2]) , dtype = float)

    # output vector
    y = np.array( ([75], [82], [93]) , dtype = float)

    # scale the input and output data
    X = X / np.amax(X,axis=0)
    y = y / 100

    # define network parameters
    size_input = np.shape(X)[1] # number of columns of X
    size_hidden = 3
    size_output = 1

    # Create the weights
    np.random.seed(16)
    W1 = np.random.randn(size_input, size_hidden)
    W2 = np.random.randn(size_hidden, size_output)

    # A dot product of the weights by the inputs provides the values for the next layer (z)
    z2 = np.dot(X, W1)
    a2 = sigmoid(z2)

    z3 = np.dot(a2, W2)
    y_hat = sigmoid(z3)
    # return y_hat

    # e.g 1:
    y = np.array([[1], [2]])
    y_hat = np.array([[1], [2]])
    print(cost(y, y_hat)) # should be zero as y is the same as y_hat
    # e.g 2:
    y = np.array([[1], [2]])
    y_hat = np.array([[2], [2]])
    print(cost(y, y_hat)) # should be non-zero as y is not the same as y_hat


if __name__ == '__main__':
    main()

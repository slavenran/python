import numpy as np
from random import random

# save activations and derivatives
# implement backpropagation
# implement gradient descent
# implement training
# train our net with some dummy dataset
# make some predictions

class MLP:
    """A Multilayer Perceptron class.
    """
    def __init__(self, num_inputs=3, num_hidden=[3, 5], num_outputs=2):
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs

        # creates a generic representation of the layers
        layers = [self.num_inputs, *self.num_hidden, self.num_outputs]

        # initiate random weights for the layers
        self.weights = []
        for i in range(len(layers)-1):
            w = np.random.rand(layers[i], layers[i+1])  # pravi matricu veza izmedju svakog lejera sa random tezinama izmedju 0 i 1
            self.weights.append(w)

        activations = []
        for i in range(len(layers)):
            a = np.zeros(layers[i])
            activations.append(a)
        self.activations = activations

        derivatives = []
        for i in range(len(layers)-1):
            d = np.zeros((layers[i], layers[i+1]))
            derivatives.append(d)
        self.derivatives = derivatives

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward_propagate(self, inputs):
        activations = inputs
        self.activations[0] = inputs

        for i, w in enumerate(self.weights):
            # calculate matrix multiplication between previous activation and weight matrix
            net_inputs = np.dot(activations, w)

            #apply sigmoid activation function
            activations = self._sigmoid(net_inputs)
            self.activations[i+1] = activations
        return activations

    def back_propagate(self, error, verbose=False):

        # dE/dW_i = (y - a_[i+1]) s'(h_[i+1]) a_i
        # s'(h_[i+1]) = s(h_[i+1])(1 - s(h_[i+1]))
        # s(h_[i+1]) = a_[i+1]

        # dE/dW_[i-1] = (y - a_[i+1]) s'(h_[i+1]) W_i s'(h_i) a_[i-1]

        for i in reversed(range(len(self.derivatives))):            # go backwards
            activations = self.activations[i+1]
            delta = error * self._sigmoid_derivative(activations)   # ndarray([0.1, 0.2]) --> ndarray([[0.1, 0.2]])
            delta_reshaped = delta.reshape(-1, 1).T                 # or just delta.reshape(1, -1)
            current_activation = self.activations[i]                # ndarray([0.1, 0.2]) --> ndarray([[0.1], [0.2]])
            current_activation_reshaped = current_activation.reshape(-1, 1)

            self.derivatives[i] = np.dot(current_activation_reshaped, delta_reshaped)
            error = np.dot(delta, self.weights[i].T)

            if verbose: print(f"Derivatives for W{i}:", self.derivatives[i])

        return error

    def gradient_descent(self, learning_rate):
        for i in range(len(self.weights)):
            weights = self.weights[i]
            # print("Original W{} {}".format(i, weights))

            derivatives = self.derivatives[i]

            weights += derivatives * learning_rate
            # print("Updated W{} {}".format(i, weights))

    def train(self, inputs, targets, epochs, learning_rate):
        for i in range(epochs):
            sum_error = 0
            for input, target in zip(inputs, targets):
                # perform forward prop
                output = self.forward_propagate(input)

                # calculate error
                error = target - output

                # back propagation
                self.back_propagate(error)

                # apply gradient descent
                self.gradient_descent(learning_rate)

                sum_error += self._mse(target, output)

            # report error
            print("Error: {} at epoch {}".format(sum_error / len(inputs), i))

    def _mse(self, target, output):
        return np.average((target - output)**2)


if __name__ == "__main__":
    # create a dataset to train a network for the sum operation
    inputs = np.array([[random() / 2 for _ in range(2)] for _ in range(1000)])  # array([[0.1, 0.2], [0.3, 0.4]])
    targets = np.array([[i[0] + i[1]] for i in inputs])                         # array([[0.3], [0.7]])

    # create an MLP
    mlp = MLP(2, [3], 1)

    # train our MLP
    mlp.train(inputs, targets, 50, 0.1)

    # create dummy data
    input = np.array([0.5, 0.1])
    target = np.array([0.6])

    output = mlp.forward_propagate(input)
    print("\n\nOur network believes the result is", output)
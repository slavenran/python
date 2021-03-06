import numpy as np

class MLP:
    def __init__(self, num_inputs=3, num_hidden=[3, 5], num_outputs=2):
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs

        layers = [self.num_inputs, *self.num_hidden, self.num_outputs]

        # initiate random weights
        self.weights = []
        for i in range(len(layers)-1):
            w = np.random.rand(layers[i], layers[i+1])  # pravi matricu veza izmedju svakog lejera sa random tezinama izmedju 0 i 1
            self.weights.append(w)

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward_propagate(self, inputs):
        activations = inputs

        for w in self.weights:
            # calc net inputs
            net_inputs = np.dot(activations, w)

            #calc the activations
            activations = self._sigmoid(net_inputs)

        return activations


if __name__ == "__main__":
    # create an MLP
    mlp = MLP()

    # create some inputs
    inputs = np.random.rand(mlp.num_inputs)

    # perform forward prop
    outputs = mlp.forward_propagate(inputs)

    # print the results
    print("The net input:", inputs)
    print("The net output:", outputs)

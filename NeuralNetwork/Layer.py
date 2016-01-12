import random


class Layer:
    def __init__(self, tmp_num_nodes, tmp_num_inputs, activation_fun):
        super(Layer, self).__init__()
        self.numNodes = tmp_num_nodes
        self.numInputs = tmp_num_inputs
        self.output = [0] * self.numNodes
        self.weightedSum = [0] * self.numNodes
        self.weightMatrix = []
        self.activationFun = activation_fun
        for i in range(0, self.numInputs):
            self.weightMatrix.append([])
            for j in range(0, self.numNodes):
                self.weightMatrix[i].append(random.random() / 2 - 0.25)

    def calculate_output(self, input):
        for j in range(0, self.numNodes):
            somma = [0] * self.numNodes
            for i in range(0, self.numInputs):
                somma[j] += self.weightMatrix[i][j] * float(input[i])
            self.weightedSum[j] = somma[j]

            self.output[j] = self.activationFun(self.weightedSum[j])

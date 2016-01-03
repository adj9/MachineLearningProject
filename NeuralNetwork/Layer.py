import random

__author__ = 'Daniele'


class Layer:
    def __init__(self, tmpNumNodes, tmpNumInputs, activationFun):
        super(Layer, self).__init__()
        self.numNodes = tmpNumNodes
        self.numInputs = tmpNumInputs
        self.output = [0] * self.numNodes
        self.weightedSum = [0] * self.numNodes
        self.weightMatrix = []
        self.activationFun = activationFun
        for i in range(0, self.numInputs):  # +1):
            self.weightMatrix.append([])
            for j in range(0, self.numNodes):
                self.weightMatrix[i].append(random.random() / 2 - 0.25)

    def calculateOutput(self, input):
        for j in range(0, self.numNodes):
            somma = [0] * self.numNodes
            for i in range(0, self.numInputs):
                somma[j] += self.weightMatrix[i][j] * float(input[i])
            self.weightedSum[j] = somma[j]  # - self.weightMatrix[i+1][j] # sostanzialmente viene tolto il bias

            self.output[j] = self.activationFun(self.weightedSum[j])

class Layer:
    "Layer of network"
    def __init__(self, inputs, numNodes):
        super(Layer, self).__init__()
        self.__inputs = inputs
        self.__matrix = []

    def generateMatrix(self):
        for i in range(1, len(self.__inputs)):
            self.__matrix[i-1] = [self.input[i].getWeights]


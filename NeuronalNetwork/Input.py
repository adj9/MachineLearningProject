class Input:
    def __init__(self, value, weights):
        super(Input, self).__init__()
        self.__value = value
        self.__weights = []

    def getValue(self):
        return self.__value

    def getWeights(self):
        return self.__weights

    def getIndexWheight(self, index):
        return self.__weights[index]
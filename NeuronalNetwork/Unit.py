class Unit:
    "Unit of network"
    def __init__(self, weights, threshold, activatingFunction):
        super(Unit, self).__init__()
        self.__inputs = []
        self.__previous = []
        self.__weights = weights
        self.__output = ""
        self.__value = ""
        self.__threshold = threshold
        self.__activatingFunction = activatingFunction

    def addPrevious(self, previou):
        self.__previous.append(previou)

    def setInput(self, input):
        self.__inputs = input

    def setOutput(self):
        param = 0
        if self.__previous == []:
            self.addPrevious(self.__inputs)
            for i in range(1, len(self.__previous[0])):
                param = param + (self.__previous[0].getIndexWeight(i) * self.__inputs[i])
        else:
            param = 0
            for i in range(0, len(self.__previous)):
                param = param + (self.__previous[i].getWeight() * self.__inputs[i])

        self.__output = self.__activatingFunction(param)

    def getOutput(self):
        print(self.__output)

    def getWeight(self):
        return self.__weight

    def changeWeight(self, weight):
        self.__weight = weight

    def getThreshold(self):
        return self.__threshold



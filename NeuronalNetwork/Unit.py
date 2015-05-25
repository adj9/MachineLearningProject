class Unit:
    "Unit of network"
    def __init__(self, weight, threshold, activatingFunction):
        super(Unit, self).__init__()
        self.__previous = []
        self.__weight = weight
        self.__threshold = threshold
        self.__activatingFunction = activatingFunction

    def addPrevious(self, previou):
        self.__previous.append(previou)

    def setWeight(self):
        if self.__previous == []:
            self.__weight = -1
        else:
            #for i in range(0, len(self.__previous)):
                #if self.__previous[i].getWeight() < self.__threshold:
                    #self.__previous[i].changeWeight(-1 * self.__previous[i].getWeight())

            param = 0
            for i in range(0, len(self.__previous)):
                param = param + (self.__previous[i].getWeight() * self.__weight)

            self.__weight = self.__activatingFunction(param)

    def getWeight(self):
        return self.__weight

    def changeWeigh(self, weight):
        self.__weight = weight

    def getThreshold(self):
        return self.__threshold



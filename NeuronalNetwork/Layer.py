import Unit
from Unit import *

class Layer:
    "Layer of network"
    def __init__(self):
        super(Layer, self).__init__()
        self.__components = []
        self.__previous = []

    def addComponent(self, component):
        self.__components.append(component)

    def getWeight(self):
        weight = 0
        for i in range(0, len(self.__components)):
            weight = weight + self.__components[i].getWeight()

        return weight

    def indexUnit(self, index):
        return self.__components[index - 1]

    def __len__(self):
        return len(self.__components)


# La weights matrix risultante è strutturata in questo modo:
# Layer di Input
# 1° Layer nascosto
#        ...
# n° Layer nascosto
# Layer di Output
#
# Ha numenone numberLayer x numberLayer

class Network:
    ""
    def __init__(self):
        super(Network, self).__init__()
        self.__layers = []

    def add_layer(self, layer):
        self.__layers.append(layer)

    def addLayer(self, layer):
        self.__layers.append(layer)

    def get_layer(self, index):
        return self.__layers[index]

    def countLayers(self):
        return len(self.__layers)

    # def generateWeightMatrix(self):
    #     width = len(self.__layers[0])
    #     for i in range(1, len(self.__layers)):
    #         if width < len(self.__layers[i]):
    #             width = len(self.__layers[i])
    #
    #     matrix = []
    #     print('righe = ', len(self.__layers), ' , colonne = ', width)
    #     for i in range(0, len(self.__layers)):
    #         line = []
    #         print('righe = ', len((self.__layers)))
    #         for j in  range(0, len(self.__layers[i])):
    #             print('j: ', j)
    #             print('colonne = ', len(self.__layers[i]))
    #             line.append(self.__layers[i].indexUnit(j).getWeight())
    #             print('weight unit = ', self.__layers[i].indexUnit(j).getWeight())
    #         if len(line) < width:
    #             for j in range(len(line), width):
    #                 line.append(0)
    #         matrix.append(line)
    #
    #     return matrix, len(self.__layers), width


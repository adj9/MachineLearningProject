class Layer:
    # dal secondo layer in poi gli inputs sono i value dei previous
    "Layer of network"
    def __init__(self, inputs):
        super(Layer, self).__init__()
        #self.__units = []
        self.__inputs = inputs
        self.__matrix = []

    # def set_units(self, units):
    #     self.__units.append(units)
    #
    # def get_unit(self, index):
    #     return self.__units[index]

    def get_weights_in(self, index):
        result = []
        for i in range (0, len(self.__inputs)):
            result.append(self.__inputs[i].get_index_weight(index))

        return result

    def generate_matrix(self):
        #if self.__units == 0:
            for i in range(0, len(self.__inputs)-1):
                self.__matrix.append(self.__inputs[i].get_weights())
        # else:
        #     for i in range(0, len(self.__units)):
        #         self.__matrix[i] = [self.__units[i].get_weight_out()]

    def get_matrix(self):
        return self.__matrix

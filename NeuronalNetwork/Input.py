class Input:
    def __init__(self, value, weights):
        super(Input, self).__init__()
        self.__value = value
        self.__weights = weights

    def get_value(self):
        return self.__value

    def get_weights(self):
        return self.__weights

    def get_index_weight(self, index):
        return self.__weights[index]
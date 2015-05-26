class Unit:
    "Unit of network"
    def __init__(self, weightsIn, threshold, activatingFunction):
        super(Unit, self).__init__()
        self.__previous = []
        self.__weightsIn = weightsIn
        self.__weightOut = ""
        self.__value = "" #valore della funzione di attivazione f(a) con a = somma pesata dei pesi in ingresso e dei values dei nodi precedenti
        self.__threshold = threshold
        self.__localInput = -1
        self.__activatingFunction = activatingFunction

    def set_previous(self, previou):
        self.__previous.append(previou)

    def get_previous(self, index):
        return self.__previous[index]

    def set_weights_in(self, weights):
        self.__weightsIn = weights

    def get_index_weight(self, index):
        return self.__weightsIn[index]

    def get_weights(self):
        return self.__weightsIn

    def set_weight_out(self, weight):
        self.__weightOut = weight

    def get_weight_out(self):
        return self.__weightOut

    def set_value(self):
        param = (self.__threshold * self.__localInput)
        # if self.__previous == []:
        #     self.addPrevious(self.__inputs)
        #     for i in range(1, len(self.__previous[0])):
        #         param = param + (self.__previous[0].getIndexWeight(i) * self.__inputs[i])
        # else:

        for i in range(0, len(self.__previous)):
            param = param + (self.__previous[i].get_value() * self.__weightsIn[i])

        self.__value = self.__activatingFunction(param)

    def get_value(self):
        return self.__value



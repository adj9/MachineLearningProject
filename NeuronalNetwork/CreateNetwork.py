__author__ = 'Alessandro'

import numpy
from numpy import zeros

import Dataset.DatasetReader as reader

import NeuronalNetwork.Network as Net
from NeuronalNetwork.Network import *
import NeuronalNetwork.Layer
from NeuronalNetwork.Layer import *
import NeuronalNetwork.Unit
from  NeuronalNetwork.Unit import *


class CreateNethwork:
    def CreateNethwork(self, dataset, activating_functions):
        super(CreateNethwork, self).__init__()
        self.__dataset = reader.get_dataset(dataset)
        self.__dataset = []
        self.__numberHiddenUnit = 4
        self.__number_classes = self.__set_number_classes()
        self.__network = Net()
        self.__activating_functions = activating_functions

    def __set_number_classes(self):
        self.__number_classes = 1
        for i in range(1, len(self.__dataset) - 1):
            if self.__dataset[i][-1] != self.__number_classes[i - 1][-1]:
                self.__number_classes = self.__number_classes + 1

    def get_input_net_iris_setosa(self):
        res = zeros(self.__number_classes)
        res[0] = 1

        return res

    def get_input_net_iris_versicolor(self):
        res = zeros(self.__number_classes)
        res[1] = 1

        return res

    def get_input_net_iris_virginica(self):
        res = zeros(self.__number_classes)
        res[2] = 1

        return res

    def create_nethwork_topology(self):
        layer = Layer()
        for i in range(0, self.__numberclass - 1):
            layer.set_units(Unit(0, 1, self.__activating_functions[0]))

        # Aggiunta dello strato di input
        self.__network.add_layer(layer)

        output = layer

        for i in range(0, self.__numberHiddenUnit):
            layer.set_units(Unit(0, 1, self.__activating_functions[1]))

        # Aggiunta dello strato di intrerno che è composto da quattro unità
        self.__network.add_layer(layer)

        # Aggiunta dello strato di output
        self.__network.add_layer(output)

    def run_nethwork(self):
        pass

    def get_number_class(self):
        return self.__number_class
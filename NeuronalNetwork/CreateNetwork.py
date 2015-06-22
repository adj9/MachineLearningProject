from NeuralNetwork import Layer
from NeuralNetwork.Unit import Unit

__author__ = 'Alessandro'

import os
import csv

import NeuronalNetwork.Network as Net
from NeuronalNetwork.Network import *
from NeuronalNetwork.Layer import *
from  NeuronalNetwork.Unit import *


class CreateNethwork:
    def CreateNethwork(self, dataset, activating_functions):
        super(CreateNethwork, self).__init__()
        self.__file_parser(self.__file_parser(self._path_file(dataset)))
        self.__dataset = []
        self.__numberHiddenUnit = 4
        self.__number_class = 0
        self.__network = Net()
        self.__activating_functions = activating_functions

    def __path_file(self, dataset_name):
        current_path = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_path, dataset_name)
        return open(full_path, 'r')

    def __file_parser(self, path):
        with open(path, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                self.__dataset.apppend(row)
                not_eql = False
                for i in len(self.__dataset):
                    if row[-1] != self.__dataset[i]:
                        not_eql = True
                if not_eql:
                    self.__number_class = self.__number_class + 1

    def create_nethwork_topology(self):
        layer = Layer()
        for i in range(0, self.__numberclass - 1):
            layer.set_units(Unit(0, 1, self.__activating_functions[0]))

# Aggiunta dello strato di input
        self.__network.add_layer(layer)

        output = layer

        for i in range(0, self.__numberHiddenUnit):
            layer.set_units(Unit(0, 1, self.__activating_functions[1]))

# Aggiunta dello strato di intrerno che � composto da quattro unit�
        self.__network.add_layer(layer)

# Aggiunta dello strato di output
        self.__network.add_layer(output)

    def run_nethwork(self):
        pass

    def grt_number_class(self):
        return self.__number_class
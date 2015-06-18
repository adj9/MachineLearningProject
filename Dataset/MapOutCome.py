__author__ = 'Alessandro'

import Dataset.DatasetReader as data_reader

from Dataset import *


class MapOutCome:
    ""
    def __init__(self, fileReader):
        super(MapOutCome, self).__init__()
        self.__fileReader = data_reader.get_dataset(fileReader)
        self.__map = {'Iris-setosa\n': 0, 'Iris-versicolor\n': 0, 'Iris-virginica\n': 0}


    def set_file_path(self, fileReader):
        self.__fileReader = data_reader.get_dataset(fileReader)

    def get_path_file(self):
        return self.__fileReader.__getattribute__('name')

    def run(self):
        print('file: ', self.__fileReader)
        for row in self.__fileReader:
            outCome = row.split(',')
            self.__map[outCome[len(outCome) - 1]] = self.__map[outCome[len(outCome) - 1]] + 1
        self.__fileReader.close()

    def get_map(self):
        return self.__map

    def get_countIrisSetosa(self):
        return  self.__map['Iris-setosa']

    def get_countIrisVersicolor(self):
        return  self.__map['Iris-versicolor']

    def get_countIrisVirginica(self):
        return  self.__map['Iris-virginica']


import copy

__author__ = 'Daniele'

from ANN.Network import *
import numpy as np
import Dataset.DatasetReader as data
import math


def neural_network(dataset_train, dataset_test):
    # Prendere la colonna Target del dataset
    classiOutput = set()
    for esempio in dataset_train:
        classiOutput.add(esempio[len(esempio)-1])

    # Selezionare i Target senza duplicazione
    listaClassi = []

    for c in classiOutput:
        listaClassi.append(c)

    # Costruzione dell topologie della Rete
    lng = len(dataset_train[0])
    numeroInput = lng - 1
    # Creo l'oggetto Network
    rete = Network(numeroInput, listaClassi, math.tanh)
    # Aggiunta degli strati
    rete.addHiddenLayer(4)
    # Lo strato di Out avr� 3 unit�
    rete.addOutputLayer()
    rete.train(dataset_train)
    # ********************************************

    # Classificazione
    giuste = 0
    sbagliate = 0
    lable_learning = list()
    for test in dataset_test:
        outputClass = rete.classify(test[:len(test)-1]) #passaggio dell'input alla rete
        lable_learning.append(outputClass)
        if (outputClass==test[len(test)-1]):
            giuste += 1
            print("<",outputClass[0:len(outputClass)-1],",",test[len(test)-1],"> OK!!!")
        else:
            sbagliate +=1
            print("<",outputClass[0:len(outputClass)-1],",",test[len(test)-1],"> SBAGLIATO!")


    # Stampa della matrici parziale
    for lay in rete.layers:
        print(lay.weightMatrix)

    print("giuste ", giuste)
    print("sbagliate ", sbagliate)
#    print("accuracy ",float(giuste)/(giuste+sbagliate))
    return lable_learning
#
# reteXOR = Network(2, ['true'], funzioneSoglia)
# reteXOR.addHiddenLayer(2)
# reteXOR.addOutputLayer()
# layer0 = reteXOR.layers[0]
# layer0.weightMatrix = [[-1.0,-1.0],[-1.0,-1.0],[-1.5,-0.5]]
# layer1 = reteXOR.layers[1]
# layer1.weightMatrix = [[1],[-1],[0.5]]
# print(reteXOR.calculateOutput([1,1]))
# print(reteXOR.calculateOutput([1,0]))
# print(reteXOR.calculateOutput([0,0]))
# print(reteXOR.calculateOutput([0,1]))

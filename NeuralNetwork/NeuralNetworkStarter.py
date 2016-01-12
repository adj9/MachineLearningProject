import math

from NeuralNetwork.Network import *


def neural_network(dataset_train, dataset_test):
    # Prendere la colonna Target del dataset
    classiOutput = set()
    for esempio in dataset_train:
        classiOutput.add(esempio[len(esempio) - 1])

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
    rete.add_hidden_layer(4)
    # Lo strato di Out avrà 3 unità
    rete.add_output_layer()
    rete.train(dataset_train)

    # Classificazione
    giuste = 0
    sbagliate = 0
    lable_learning = list()
    for test in dataset_test:
        output_class = rete.classify(test[:len(test) - 1])  # Passaggio dell'input alla rete
        lable_learning.append(output_class)
        if output_class == test[len(test) - 1]:
            giuste += 1
        else:
            sbagliate += 1

    rete.close_report()
    return lable_learning

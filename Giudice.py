__author__ = 'nzarrilli'

import copy
import os
import numpy as np
import BayesianClassifier.NaiveBayes as nb
import ID3.DecisionTree as dt

from Dataset.DatasetReader import get_dataset
from NeuralNetwork.NeuralNetworkStarter import neural_network


def giudica():
    name_dataset = 'Fiori.csv'

    try:
        os.remove("report.txt")
    except OSError:
        pass

    # Recupero il dataset
    dataset = get_dataset(name_dataset)

    # Randomizzo il dataset
    np.random.shuffle(dataset)

    # Calcolo la dimensione del dataset e divido per K sottoinsiemi
    k = 10
    size_dataset = int(len(dataset) / k)

    part_dataset = list(np.ones(k))

    j = 0
    for x in range(k):
        part_dataset[x] = dataset[j:j + size_dataset]
        j += size_dataset

    #
    # K-Fold Cross Validation
    #
    accuracy = list()
    accuracy_bayes = list()
    accuracy_nn = list()
    accuracy_id3 = list()
    for i in range(k):
        dataset_train = list()
        temp_data = copy.deepcopy(part_dataset)  # copia completa
        dataset_test = temp_data.pop(i)

        for z in range(len(temp_data)):
            dataset_train += temp_data[z]

        output_naive_bayes = nb.naive_bayes(dataset_train, dataset_test)
        output_nn = neural_network(dataset_train, dataset_test)
        output_id3 = dt.blackBoxID3(copy.deepcopy(dataset_train), copy.deepcopy(dataset_test))

        ris = get_classificazione(output_naive_bayes, output_id3, output_nn)

        accuracy.append(check_accuracy(ris, dataset_test))
        accuracy_bayes.append(check_accuracy(output_naive_bayes, dataset_test))
        accuracy_nn.append(check_accuracy(output_nn, dataset_test))
        accuracy_id3.append(check_accuracy(output_id3, dataset_test))

    print('Media Naive Bayes:', round(np.average(accuracy_bayes), 3) * 100, '%')
    print('Media Neural Network:', round(np.average(accuracy_nn), 3) * 100, '%')
    print('Media ID3:', round(np.average(accuracy_id3), 3) * 100, '%')
    print('Media totale:', round(np.average(accuracy), 3) * 100, '%')


# Funzione che "giudica" la classificazione piu probabile
def get_classificazione(naive_bayes, id3, neural_network):
    classificazione = list()
    for i in range(len(naive_bayes)):
        num_setosa = 0
        num_versicolor = 0
        num_virginica = 0

        num_setosa, num_versicolor, num_virginica = incrementa_occorrenze(naive_bayes[i], num_setosa, num_versicolor,
                                                                          num_virginica)
        num_setosa, num_versicolor, num_virginica = incrementa_occorrenze(id3[i], num_setosa, num_versicolor,
                                                                          num_virginica)
        num_setosa, num_versicolor, num_virginica = incrementa_occorrenze(neural_network[i], num_setosa, num_versicolor,
                                                                          num_virginica)

        totale = [num_setosa, num_versicolor, num_virginica]

        classificazione.append(get_label(totale.index(max(totale))))

    return classificazione


def incrementa_occorrenze(dataset, num_setosa, num_versicolor, num_virginica):
    if dataset == "Iris-setosa":
        num_setosa += 1
    elif dataset == "Iris-versicolor":
        num_versicolor += 1
    else:
        num_virginica += 1

    return num_setosa, num_versicolor, num_virginica


def check_accuracy(ris, data_test):
    x = list(zip(*data_test))[-1]
    tp = 0
    fp = 0

    for i in range(len(x)):
        if x[i] == ris[i]:
            tp += 1
        else:
            fp += 1

    accuracy = tp / len(data_test)

    return accuracy


# Restituisce l'etichetta
def get_label(position):
    if position == 0:
        return "Iris-setosa"
    elif position == 1:
        return "Iris-versicolor"
    else:
        return "Iris-virginica"


if __name__ == "__main__":
    giudica()

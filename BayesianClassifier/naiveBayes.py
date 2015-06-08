__author__ = 'antoniograndinetti'
# TODO: 10 cross validation, feature selection, grafici e performance del classificatore
# TODO: capire come funziona l'algoritmo a scatola chiusa
num_bin = 10

import numpy as np

def naiveB(data_train, data_test):
    prob_cond_x = [0, 0, 0, 0]

    # Calcolo la probabilità a priori del training-set
    prob_priori = calcolaProbPriori(data_train)
    # print(prob_priori)
    # discretizzazione(dataset)

    # Calcolo la probabilità condizionata
    for i in range(4):
        prob_cond_x[i] = calcola_prob_condizionata(data_train, i)

    classificazione = list(np.ones(len(data_test)))
    # Classificazione del testing-set
    for j in range(len(data_test)):
        classificazione[j] = classificatore(data_train, data_test[13], prob_priori, prob_cond_x)
        print(classificazione[j])


    return


def calcolaProbPriori(dataset):
    ultimaColonna = list(zip(*dataset))[-1]

    numSetosa = 0
    numVersicolor = 0
    numVerginica = 0
    # esiste = []
    for i in range(len(ultimaColonna)):
        '''if ultimaColonna[i] in esiste:

            esiste[ultimaColonna[i]] = esiste[ultimaColonna[i]]+1
        else:
            esiste.append((ultimaColonna[i], 1))'''
        if ultimaColonna[i] == "Iris-setosa\n":
            numSetosa = numSetosa + 1

        elif ultimaColonna[i] == "Iris-versicolor\n":
            numVersicolor = numVersicolor + 1

        else:
            numVerginica = numVerginica + 1


    probSetosa = numSetosa / len(ultimaColonna)
    probVersicolor = numVersicolor / len(ultimaColonna)
    probVerginica = numVerginica / len(ultimaColonna)


    # print(ultimaColonna.count("Iris-setosa\n"))

    return [probSetosa, probVersicolor, probVerginica]


def discretizzazione(dataset):
    listaSetosa = []
    listaVersicolor = []
    listaVerginica = []

    for i in range(len(dataset)):

        if dataset[i][4] == "Iris-setosa\n":
            listaSetosa.append(dataset[i])

        elif dataset[i][4] == "Iris-versicolor\n":
            listaVersicolor.append(dataset[i])

        else:
            listaVerginica.append(dataset[i])

    setosa1 = list(zip(*listaSetosa))[0]
    setosa1 = [float(i) for i in setosa1]
    rangeSetosa1 = [min(setosa1), max(setosa1)]
    print(rangeSetosa1)

    setosa2 = list(zip(*listaSetosa))[1]
    setosa2 = [float(i) for i in setosa2]
    rangeSetosa2 = [min(setosa2), max(setosa2)]
    print(rangeSetosa2)

    setosa3 = list(zip(*listaSetosa))[2]
    setosa3 = [float(i) for i in setosa3]
    rangeSetosa3 = [min(setosa3), max(setosa3)]
    print(rangeSetosa3)

    setosa4 = list(zip(*listaSetosa))[3]
    setosa4 = [float(i) for i in setosa4]
    rangeSetosa4 = [min(setosa4), max(setosa4)]
    print(rangeSetosa4)

    versicolor1 = list(zip(*listaVersicolor))[0]
    versicolor1 = [float(i) for i in versicolor1]
    rangeVersicolor1 = [min(versicolor1), max(versicolor1)]
    print(rangeVersicolor1)

    versicolor2 = list(zip(*listaVersicolor))[1]
    versicolor2 = [float(i) for i in versicolor2]
    rangeVersicolor2 = [min(versicolor2), max(versicolor2)]
    print(rangeVersicolor2)

    versicolor3 = list(zip(*listaVersicolor))[2]
    versicolor3 = [float(i) for i in versicolor3]
    rangeVersicolor3 = [min(versicolor3), max(versicolor3)]
    print(rangeVersicolor3)

    versicolor4 = list(zip(*listaVersicolor))[3]
    versicolor4 = [float(i) for i in versicolor4]
    rangeVersicolor4 = [min(versicolor4), max(versicolor4)]
    print(rangeVersicolor4)

    verginica1 = list(zip(*listaVerginica))[0]
    verginica1 = [float(i) for i in verginica1]
    rangeVerginica1 = [min(verginica1), max(verginica1)]
    print(rangeVerginica1)

    verginica2 = list(zip(*listaVerginica))[1]
    verginica2 = [float(i) for i in verginica2]
    rangeVerginica2 = [min(verginica2), max(verginica2)]
    print(rangeVerginica2)

    verginica3 = list(zip(*listaVerginica))[2]
    verginica3 = [float(i) for i in verginica3]
    rangeVerginica3 = [min(verginica3), max(verginica3)]
    print(rangeVerginica3)

    verginica4 = list(zip(*listaVerginica))[3]
    verginica4 = [float(i) for i in verginica4]
    rangeVerginica4 = [min(verginica4), max(verginica4)]
    print(rangeVerginica4)

    return


def calcola_prob_condizionata(dataset, position):
    bin_x = count_bin(dataset, position)
    prob_cond_x = []

    for j in range(num_bin):
        prob_cond_x.append([0, 0, 0])

    for i in range(len(bin_x)):
        sommariga = bin_x[i][0] + bin_x[i][1] + bin_x[i][2]
        for j in range(0, 3):
            if sommariga != 0:
                prob_cond_x[i][j] = bin_x[i][j] / sommariga
            else:
                prob_cond_x[i][j] = 0

    print('----------------------------------------------------------------------------------------------------------')

    return prob_cond_x


def count_bin(dataset, position):
    bin_x = []

    for j in range(num_bin):
        bin_x.append([0, 0, 0])

    x = list(zip(*dataset))[position]
    x = [float(i) for i in x]
    min_x = min(x)
    max_x = max(x)
    grandezza_bin = (max_x - min_x) / num_bin

    for i in range(len(dataset)):
        start_bin = min_x
        for j in range(1, num_bin + 1):
            end_bin = min_x + grandezza_bin * j

            if (j < num_bin) & (float(dataset[i][position]) >= start_bin) & (float(dataset[i][position]) < end_bin):
                bin_x = increase_bin(dataset[i][4], bin_x, j - 1)
            elif (float(dataset[i][position]) >= start_bin) & (float(dataset[i][position]) <= end_bin):
                bin_x = increase_bin(dataset[i][4], bin_x, j - 1)

            start_bin = end_bin

    return bin_x


def increase_bin(dataset, bin_x, i):
    if dataset == "Iris-setosa\n":
        bin_x[i][0] += 1
    elif dataset == "Iris-versicolor\n":
        bin_x[i][1] += 1
    else:
        bin_x[i][2] += 1

    return bin_x


def trova_bin(dataset, position, element):
    x = list(zip(*dataset))[position]
    x = [float(i) for i in x]
    min_x = min(x)
    max_x = max(x)
    grandezza_bin = (max_x - min_x) / num_bin

    for i in range(len(dataset)):
        start_bin = min_x
        for j in range(1, num_bin + 1):
            end_bin = min_x + grandezza_bin * j

            if (j < num_bin) & (float(element) >= start_bin) & (float(element) < end_bin):
                return j - 1
            elif (float(element) >= start_bin) & (float(element) <= end_bin):
                return j - 1

            start_bin = end_bin

    return None


def classificatore(dataset, x, prob_priori, prob_condizionate):
    indice = [0, 0, 0, 0]

    # Inizializzo le probabilità iniziali a posteriori a 1
    prob_post_setosa = 1
    prob_post_versicolor = 1
    prob_post_virginica = 1

    # Calcolo le probabilità a posteriori
    for i in range(4):
        indice[i] = trova_bin(dataset, i, x[i])
        prob_post_setosa = prob_condizionate[i][indice[i]][0] * prob_post_setosa
        prob_post_versicolor = prob_condizionate[i][indice[i]][1] * prob_post_versicolor
        prob_post_virginica = prob_condizionate[i][indice[i]][2] * prob_post_virginica

    prob_setosa = round(prob_priori[0] * prob_post_setosa, 3)
    prob_versicolor = round(prob_priori[1] * prob_post_versicolor, 3)
    prob_virginica = round(prob_priori[2] * prob_post_virginica, 3)

    listaProb = [prob_setosa, prob_versicolor, prob_virginica]

    return max(listaProb)

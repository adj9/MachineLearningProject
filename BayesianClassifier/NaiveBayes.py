__author__ = 'antoniograndinetti'
# TODO: feature selection, grafici e performance del classificatore
# TODO: capire come funziona l'algoritmo a scatola chiusa
num_bin = 10

import numpy as np


def naive_bayes(data_train, data_test):
    prob_cond_x = [0, 0, 0, 0]

    # Calcolo la probabilità a priori del training-set
    prob_priori = calcolaProbPriori(data_train)

    # Calcolo la probabilità condizionata
    for i in range(4):
        prob_cond_x[i] = calcola_prob_condizionata(data_train, i)

    classificazione = list(np.ones(len(data_test)))
    # Classificazione del testing-set
    for j in range(len(data_test)):
        classificazione[j] = classificatore(data_train, data_test[j], prob_priori, prob_cond_x)

    #calcola_accuratezza(classificazione, data_test)

    return calcola_accuratezza(classificazione, data_test)

# Calcolo le probabilità a priori

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

# Calcolo le probabilità condizionate

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

    return prob_cond_x

#

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

# Conta il numero di occorrenze dei target nel training-set

def increase_bin(target_train, bin_x, i):
    if target_train == "Iris-setosa\n":
        bin_x[i][0] += 1
    elif target_train == "Iris-versicolor\n":
        bin_x[i][1] += 1
    else:
        bin_x[i][2] += 1

    return bin_x


# Trova in quale BIN si trova l'attributo dell'istanza in classificazione
# Restituisce l'indice del BIN in cui si trova l'attributo, altrimenti None

def trova_bin(dataset_train, position, attributo):
    x = list(zip(*dataset_train))[position]
    x = [float(i) for i in x]
    min_x = min(x)
    max_x = max(x)
    grandezza_bin = (max_x - min_x) / num_bin

    for i in range(len(dataset_train)):
        start_bin = min_x
        for j in range(1, num_bin + 1):
            end_bin = min_x + grandezza_bin * j

            if (j < num_bin) & (float(attributo) >= start_bin) & (float(attributo) < end_bin):
                return j - 1
            elif (float(attributo) >= start_bin) & (float(attributo) <= end_bin):
                return j - 1

            start_bin = end_bin

    return None


# Classifica l'attributo x

def classificatore(dataset_train, attributo, prob_priori, prob_condizionate):
    indice = [0, 0, 0, 0]

    # Inizializzo le probabilità iniziali a posteriori a 1
    prob_post_setosa = 1
    prob_post_versicolor = 1
    prob_post_virginica = 1

    # Calcolo le probabilità a posteriori
    for i in range(4):
        indice[i] = trova_bin(dataset_train, i, attributo[i])
        # Controllo se l'attributo rientra in un BIN
        if indice[i] is not None:
            prob_post_setosa = prob_condizionate[i][indice[i]][0] * prob_post_setosa
            prob_post_versicolor = prob_condizionate[i][indice[i]][1] * prob_post_versicolor
            prob_post_virginica = prob_condizionate[i][indice[i]][2] * prob_post_virginica

    prob_setosa = round(prob_priori[0] * prob_post_setosa, 3)
    prob_versicolor = round(prob_priori[1] * prob_post_versicolor, 3)
    prob_virginica = round(prob_priori[2] * prob_post_virginica, 3)

    # Lista delle probabilità a posteriori del singolo attributo
    listaProb = [prob_setosa, prob_versicolor, prob_virginica]

    # Restituisco il Max delle probabilità a posteriori dell'attributo ed il suo indice
    return max(listaProb), listaProb.index(max(listaProb))

# Calcolo l'accuratezza

def calcola_accuratezza(classificazione, data_test):

    x = list(zip(*data_test))[-1]
    classe = np.ones(len(x))
    for i in range(len(x)):
        if x[i] == "Iris-setosa\n":
            classe[i] = 0
        elif x[i] == "Iris-versicolor\n":
            classe[i] = 1
        else:
            classe[i] = 2

    tp = 0
    tn = 0

    for i in range(len(classe)):
       if classificazione[i][1] == classe[i]:
           tp += 1
       else:
           tn += 1

    accurancy = tp  / len(data_test)
    #print('Accurancy', tp, '/', len(data_test))


    return accurancy
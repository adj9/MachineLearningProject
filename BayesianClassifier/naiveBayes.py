__author__ = 'antoniograndinetti'

num_bin = 10

def naiveB(dataset):
    # calcolaProbPriori(dataset)
    # discretizzazione(dataset)
    calcolaDiscreto(dataset)

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

    print(numSetosa)
    print(numVersicolor)
    print(numVerginica)

    probSetosa = numSetosa / len(ultimaColonna)
    probVersicolor = numVersicolor / len(ultimaColonna)
    probVerginica = numVerginica / len(ultimaColonna)

    print(probSetosa)
    # print(ultimaColonna.count("Iris-setosa\n"))


    return

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

def calcolaDiscreto(dataset):

    bin_x1 = countBin(dataset,0)
    prob_cond_x1 = []

    for j in range(num_bin):
        prob_cond_x1.append([0, 0, 0])

    for i in range(len(bin_x1)):
        sommariga = bin_x1[i][0] + bin_x1[i][1] + bin_x1[i][2]
        for j in range(0,3):
            prob_cond_x1[i][j] = bin_x1[i][j]/sommariga

    print(bin_x1)
    print(prob_cond_x1)

    return

def countBin(dataset, position):
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

            if (j < num_bin) & (float(dataset[i][0]) >= start_bin) & (float(dataset[i][0]) < end_bin):
                if dataset[i][4] == "Iris-setosa\n":
                    bin_x[j - 1][0] += 1
                elif dataset[i][4] == "Iris-versicolor\n":
                    bin_x[j - 1][1] += 1
                else:
                    bin_x[j - 1][2] += 1
            elif (float(dataset[i][0]) >= start_bin) & (float(dataset[i][0]) <= end_bin):
                if dataset[i][4] == "Iris-setosa\n":
                    bin_x[j - 1][0] += 1
                elif dataset[i][4] == "Iris-versicolor\n":
                    bin_x[j - 1][1] += 1
                else:
                    bin_x[j - 1][2] += 1

            start_bin = end_bin

    return bin_x

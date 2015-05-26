__author__ = 'antoniograndinetti'

numeroBin = 10

def naiveB(dataset):
    #calcolaProbPriori(dataset)
    #discretizzazione(dataset)
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
            numVersicolor = numVersicolor +1

        else:
            numVerginica = numVerginica + 1


    print(numSetosa)
    print(numVersicolor)
    print(numVerginica)

    probSetosa = numSetosa/len(ultimaColonna)
    probVersicolor = numVersicolor/len(ultimaColonna)
    probVerginica = numVerginica/len(ultimaColonna)

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

    colonna1 = list(zip(*dataset))[0]
    colonna1 = [float(i) for i in colonna1]
    rangeColonna1 = [min(colonna1), max(colonna1)]
    grandezzaBinX1 = (rangeColonna1[1] - rangeColonna1[0])/numeroBin

    binX1 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

    for i in range(len(dataset)):
        if (float(dataset[i][0]) >= rangeColonna1[0]) & (float(dataset[i][0]) < rangeColonna1[0]+grandezzaBinX1):
            if dataset[i][4] == "Iris-setosa\n":
                binX1[0][0] = binX1[0][0] + 1
            elif dataset[i][4] == "Iris-versicolor\n":
                binX1[0][1] = binX1[0][1] + 1
            else:
                binX1[0][2] = binX1[0][2] + 1

        elif (float(dataset[i][0]) >= rangeColonna1[0]+grandezzaBinX1) & (float(dataset[i][0]) < rangeColonna1[0]+grandezzaBinX1*2):
            if dataset[i][4] == "Iris-setosa\n":
                binX1[1][0] = binX1[1][0] + 1
            elif dataset[i][4] == "Iris-versicolor\n":
                binX1[1][1] = binX1[1][1] + 1
            else:
                binX1[1][2] = binX1[1][2] + 1

        elif (float(dataset[i][0]) >= rangeColonna1[0]+grandezzaBinX1*2) & (float(dataset[i][0]) < rangeColonna1[0]+grandezzaBinX1*3):
            if dataset[i][4] == "Iris-setosa\n":
                binX1[2][0] = binX1[2][0] + 1
            elif dataset[i][4] == "Iris-versicolor\n":
                binX1[2][1] = binX1[2][1] + 1
            else:
                binX1[2][2] = binX1[2][2] + 1

        elif (float(dataset[i][0]) >= rangeColonna1[0]+grandezzaBinX1*3) & (float(dataset[i][0]) < rangeColonna1[0]+grandezzaBinX1*4):
            if dataset[i][4] == "Iris-setosa\n":
                binX1[3][0] = binX1[3][0] + 1
            elif dataset[i][4] == "Iris-versicolor\n":
                binX1[3][1] = binX1[3][1] + 1
            else:
                binX1[3][2] = binX1[3][2] + 1

        elif (float(dataset[i][0]) >= rangeColonna1[0]+grandezzaBinX1*4) & (float(dataset[i][0]) < rangeColonna1[0]+grandezzaBinX1*5):
            if dataset[i][4] == "Iris-setosa\n":
                binX1[4][0] = binX1[4][0] + 1
            elif dataset[i][4] == "Iris-versicolor\n":
                binX1[4][1] = binX1[4][1] + 1
            else:
                binX1[4][2] = binX1[4][2] + 1

        elif (float(dataset[i][0]) >= rangeColonna1[0]+grandezzaBinX1*5) & (float(dataset[i][0]) < rangeColonna1[0]+grandezzaBinX1*6):
            if dataset[i][4] == "Iris-setosa\n":
                binX1[5][0] = binX1[5][0] + 1
            elif dataset[i][4] == "Iris-versicolor\n":
                binX1[5][1] = binX1[5][1] + 1
            else:
                binX1[5][2] = binX1[5][2] + 1

        elif (float(dataset[i][0]) >= rangeColonna1[0]+grandezzaBinX1*6) & (float(dataset[i][0]) < rangeColonna1[0]+grandezzaBinX1*7):
            if dataset[i][4] == "Iris-setosa\n":
                binX1[6][0] = binX1[6][0] + 1
            elif dataset[i][4] == "Iris-versicolor\n":
                binX1[6][1] = binX1[6][1] + 1
            else:
                binX1[6][2] = binX1[6][2] + 1

        elif (float(dataset[i][0]) >= rangeColonna1[0]+grandezzaBinX1*7) & (float(dataset[i][0]) < rangeColonna1[0]+grandezzaBinX1*8):
            if dataset[i][4] == "Iris-setosa\n":
                binX1[7][0] = binX1[7][0] + 1
            elif dataset[i][4] == "Iris-versicolor\n":
                binX1[7][1] = binX1[7][1] + 1
            else:
                binX1[7][2] = binX1[7][2] + 1

        elif (float(dataset[i][0]) >= rangeColonna1[0]+grandezzaBinX1*8) & (float(dataset[i][0]) < rangeColonna1[0]+grandezzaBinX1*9):
            if dataset[i][4] == "Iris-setosa\n":
                binX1[8][0] = binX1[8][0] + 1
            elif dataset[i][4] == "Iris-versicolor\n":
                binX1[8][1] = binX1[8][1] + 1
            else:
                binX1[8][2] = binX1[8][2] + 1

        elif (float(dataset[i][0]) >= rangeColonna1[0]+grandezzaBinX1*9) & (float(dataset[i][0]) <= rangeColonna1[0]+grandezzaBinX1*10):
            if dataset[i][4] == "Iris-setosa\n":
                binX1[9][0] = binX1[9][0] + 1
            elif dataset[i][4] == "Iris-versicolor\n":
                binX1[9][1] = binX1[9][1] + 1
            else:
                binX1[9][2] = binX1[9][2] + 1


    probCondX1 = binX1

    print(binX1)

    for i in range(len(binX1)):
        sommariga=binX1[i][0]+binX1[i][1]+binX1[i][2]
        for j in range(0,3):
            probCondX1[i][j]=binX1[i][j]/sommariga
            print(probCondX1[i][j])

    print(probCondX1)

    return

__author__ = 'antoniograndinetti'


def naiveB(dataset):
    calcolaProbPriori(dataset)

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
            numVerginica = numVerginica+1



    print(numSetosa)
    print(numVersicolor)
    print(numVerginica)

    probSetosa = numSetosa/len(ultimaColonna)
    probVersicolor = numVersicolor/len(ultimaColonna)
    probVerginica = numVerginica/len(ultimaColonna)

    print(probSetosa)
    # print(ultimaColonna.count("Iris-setosa\n"))


    return

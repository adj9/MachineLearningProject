__author__ = 'protoman2'

from sklearn import tree
# import numpy as np
# import Dataset.DatasetReader as reader

# name_dataset = 'Fiori.csv'
#
# #IMPORTAZIONE DATASET
# dataset = reader.get_dataset(name_dataset)
# #RANDOM DATASET
# np.random.shuffle(dataset)
# #DIVISIONE IN DUE INSIEMI TRAIN-TEST => DA SISTEMARE POI PER QUANDO RIGUARDA LA PARTE DELLA CROSS VALIDATION
# dataset_train = dataset[1:140]
# dataset_test = dataset[141:150]
#
# print("DATASET TRAIN")
# print(dataset_train)
# print('----')
#
# print("DATASET TEST CON TARGET")
# print(dataset_test)
# print('----')
#
# #INSIEME ETICHETTE DEL TRAIN SET
# target = list(zip(*dataset_train))[-1]
#
# #ELIMINAZIONE DELLA COLONNA DEL TARGET DAL DATASET DI TRAIN, PERCHè ALGORITMO clf.fit(dataset_Train, target)
# # VUOLE SOLO PASSATO COME PARAMETRO :
# #1) LE COLONNE DEGLI ATTRIBUTI
# #2) LA COLONNA DEL TARGET
# for x1 in dataset_train:
#     del x1[-1]
#
# #ELIMINAZIONE DELLA COLONNA DEL TARGET DAL DATASET DI TEST, PERCHè ALGORITMO clf.predict(dataset_test)
# for i in dataset_test:
#     del i[-1]
#
# #CREATO IL MODELLO DI CLASSIFICATORE
# clf = tree.DecisionTreeClassifier()
# #FASE DI TRAIN DEL MODELLO DI CLASSIFICAZIONE clf
# clf = clf.fit(dataset_train, target)
# # TESTING
# #LISTA DELLE ETICHETTE PREDETTE
# listaPredizione = clf.predict(dataset_test)
# print("PREDIZIONE ETICHETTE")
# print(listaPredizione)
# print('----')
# print("PREDIZIONE PROBABILITA'")
# print(clf.predict_proba(dataset_test))


def blackBoxID3(dataset_train, dataset_test):
    #INSIEME ETICHETTE DEL TRAIN SET
    target = list(zip(*dataset_train))[-1]

    #ELIMINAZIONE DELLA COLONNA DEL TARGET DAL DATASET DI TRAIN, PERCHè ALGORITMO clf.fit(dataset_Train, target)
    # VUOLE SOLO PASSATO COME PARAMETRO :
    #1) LE COLONNE DEGLI ATTRIBUTI
    #2) LA COLONNA DEL TARGET
    for x1 in dataset_train:
        del x1[-1]

    #ELIMINAZIONE DELLA COLONNA DEL TARGET DAL DATASET DI TEST, PERCHè ALGORITMO clf.predict(dataset_test)
    for i in dataset_test:
        del i[-1]

    #CREATO IL MODELLO DI CLASSIFICATORE
    clf = tree.DecisionTreeClassifier()
    #FASE DI TRAIN DEL MODELLO DI CLASSIFICAZIONE clf
    clf = clf.fit(dataset_train, target)
    # TESTING
    #LISTA DELLE ETICHETTE PREDETTE
    return clf.predict(dataset_test)
    # print("PREDIZIONE ETICHETTE")
    # print(listaPredizione)
    # print('----')
    # print("PREDIZIONE PROBABILITA'")
    # print(clf.predict_proba(dataset_test))





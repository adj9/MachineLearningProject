__author__ = 'protoman2'

from sklearn import tree

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





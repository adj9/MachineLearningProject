from sklearn import tree


def black_box_id3(dataset_train, dataset_test):
    # Insieme etichette del train set
    target = list(zip(*dataset_train))[-1]

    # Eliminazione della colonna del target dal dataset di train, perché l'algoritmo clf.fit(dataset_Train, target)
    # Vuole i seguenti parametri :
    # 1) le colonne degli attirbuti
    # 2) la colonna del target
    for x1 in dataset_train:
        del x1[-1]

    # Eliminazione della colonna del target dal dataset di test, perché l'algoritmo clf.predict(dataset_test)
    for i in dataset_test:
        del i[-1]

    # Creato il modello di classificazione
    clf = tree.DecisionTreeClassifier()
    # Fase di train del modello di classificazione clf
    clf = clf.fit(dataset_train, target)
    # TESTING
    # Lista delle etichette predette
    return clf.predict(dataset_test)

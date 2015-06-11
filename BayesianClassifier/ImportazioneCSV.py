__author__ = 'Riccardo Perego'

import numpy as np

import BayesianClassifier.NaiveBayes as nb
import Dataset.DatasetReader as data
import matplotlib.pyplot as plt


name_dataset = 'Fiori.csv'

avg = list()

# # Feature Importance
# from sklearn import datasets
# from sklearn import metrics
# from sklearn.ensemble import ExtraTreesClassifier
# # load the iris datasets
# dataset = datasets.load_iris()
# # fit an Extra Trees model to the data
# model = ExtraTreesClassifier()
# model.fit(dataset.data, dataset.target)
# # display the relative importance of each attribute
# print(model.feature_importances_)
# #print(dataset)
#
# # Recursive Feature Elimination
# from sklearn import datasets
# from sklearn.feature_selection import RFE
# from sklearn.linear_model import LogisticRegression
# # load the iris datasets
# dataset = datasets.load_iris()
# # create a base classifier used to evaluate a subset of attributes
# model = LogisticRegression()
# # create the RFE model and select 3 attributes
# rfe = RFE(model, 3)
# rfe = rfe.fit(dataset.data, dataset.target)
# # summarize the selection of the attributes
# print(rfe.support_)
# print(rfe.ranking_)

for m in range(4):

    avg = []
    for j in range(100):

        # Importazione file CSV
        reader = data.get_dataset(name_dataset)

        # Lettura file CSV
        dataset = list()
        for row in reader:
            dataset.append((row.split(',')))


#        print("....")
        np.random.shuffle(dataset)

        for row in dataset:
            del row[m]

        #print(dataset)

        # Calcolo size del dataset e divido per K sottoinsiemi
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

        accurancy = list()
        for i in range(k):
            dataset_train = list()
            temp_data = part_dataset.copy()
            dataset_test = temp_data.pop(i)

            for z in range(len(temp_data)):
                dataset_train += temp_data[z]

            accurancy.append(nb.naive_bayes(dataset_train, dataset_test))

        #print(accurancy)
        avg.append(round(np.average(accurancy),3) * 100)



        var_attr = [0,0,0]
        for s in range(3):
            #print(s)
            attrx = (list(zip(*dataset)))[s]
            attrx = [float(i) for i in attrx]
            mediaAttrx = np.mean(attrx)
            #print(mediaAttrx)
            var_attr[s] = sum([(x - mediaAttrx)**2 for x in attrx]) / len(dataset)
            #print('Varianza :', var_attr)


    print(max(avg))


# impostazione font assi
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)

# creazione canvas (le misure sono in pollici))
plt.figure(figsize=(5, 5))

# disegno grafico
plt.plot([1,2,3,4,5], [10,20,30,40,50])

# titolo grafico
plt.title("test")

# salvataggio su file
plt.savefig("example.png")
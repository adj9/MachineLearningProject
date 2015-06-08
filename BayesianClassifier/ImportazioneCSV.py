__author__ = 'Riccardo Perego'

import numpy as np

import BayesianClassifier.NaiveBayes as nb
import Dataset.DatasetReader as data

name_dataset = 'Fiori.csv'

# Importazione file CSV
reader = data.get_dataset(name_dataset)

# Lettura file CSV
dataset = list()
for row in reader:
    dataset.append((row.split(',')))
#
np.random.shuffle(dataset)

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

print(accurancy)
print(round(np.average(accurancy),3) * 100, '%')


var_attr = [0,0,0,0]
for s in range(4):
    print(s)
    attrx = (list(zip(*dataset)))[s]
    attrx = [float(i) for i in attrx]
    mediaAttrx = np.mean(attrx)
    print(mediaAttrx)
    var_attr[s] = sum([(x - mediaAttrx)**2 for x in attrx]) / len(dataset)
    print('Varianza :', var_attr)
    askcgòsdfbsàeivbeklwfbùwidsbvùeirwò
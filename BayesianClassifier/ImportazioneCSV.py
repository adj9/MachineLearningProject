__author__ = 'Riccardo Perego'

import BayesianClassifier.naiveBayes as nb
import numpy as np

# Importazione file CSV
reader = open('fiori.csv', 'r')

# Lettura file CSV
dataset = list()
for row in reader:
    dataset.append((row.split(',')))

# Calcolo size del dataset e divido per K sottoinsiemi
k = 10
size_dataset = int(len(dataset)/k)

part_dataset = list(np.ones(k))

j = 0
for x in range(k):
    part_dataset[x] = dataset[j:j+size_dataset]
    j += size_dataset

#
# K-Fold Cross Validation
#

for i in range(k):
    dataset_test = []
    dataset_train = []
    temp_data = part_dataset
    dataset_test.append(temp_data.pop(i))
    dataset_train.append(temp_data)

    nb.naiveB(temp_data, dataset_test)

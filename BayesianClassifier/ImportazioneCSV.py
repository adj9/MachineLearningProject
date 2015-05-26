__author__ = 'Riccardo Perego'

import BayesianClassifier.naiveBayes as nb

reader = open('fiori.csv', 'r')

attr = list()
for row in reader:
    attr.append((row.split(',')))

#print(attr)
#print(attr[0][0])

nb.naiveB(attr)

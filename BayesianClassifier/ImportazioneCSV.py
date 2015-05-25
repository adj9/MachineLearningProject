__author__ = 'Riccardo Perego'

import naiveBayes

reader = open('fiori.csv', 'r')

attr = list()
for row in reader:
    attr.append((row.split(',')))

print(attr)
print(attr[0][0])

naiveBayes.naiveB(attr)

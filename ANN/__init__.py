from ANN.Network import *
import numpy as np
import Dataset.DatasetReader as data
import math

__author__ = 'Daniele'

print('ciao Pirla')
def funzioneSoglia(x):
    if(x>=0):
        return 1
    else:
        return 0

print("ciao")
name_dataset = 'Fiori.csv'

# Importazione file CSV
dataset = data.get_dataset(name_dataset)

np.random.shuffle(dataset)

# Calcolo size del dataset e divido per K sottoinsiemi
k = 10
size_dataset = int(len(dataset) / k)
#trainSet = dataset[0: 8*size_dataset]
# testSet = dataset[8*size_dataset:]
trainSet=dataset
testSet=dataset
print("TrainSet = ", trainSet)
classiOutput = set()
for esempio in trainSet:
    classiOutput.add(esempio[len(esempio)-1])

#conversione classi da insieme a lista
listaClassi = []
for c in classiOutput.copy():
    listaClassi.append(classiOutput.pop())

esempioQualsiasi = trainSet[0]
numeroInput = len(esempioQualsiasi)-1
rete = Network(numeroInput, listaClassi, math.tanh)
rete.addHiddenLayer(4)
rete.addOutputLayer()
rete.train(trainSet)

giuste = 0
sbagliate = 0
for test in testSet:
    outputClass = rete.classify(test[:len(test)-1])
    if (outputClass==test[len(test)-1]):
        giuste += 1
        print("<",outputClass[0:len(outputClass)-1],",",test[len(test)-1],"> OK!!!")
    else:
        sbagliate +=1
        print("<",outputClass[0:len(outputClass)-1],",",test[len(test)-1],"> SBAGLIATO!")

for lay in rete.layers:
    print(lay.weightMatrix)

print("giuste ", giuste)
print("sbagliate ", sbagliate)
print("accuracy ",float(giuste)/(giuste+sbagliate))
#
# reteXOR = Network(2, ['true'], funzioneSoglia)
# reteXOR.addHiddenLayer(2)
# reteXOR.addOutputLayer()
# layer0 = reteXOR.layers[0]
# layer0.weightMatrix = [[-1.0,-1.0],[-1.0,-1.0],[-1.5,-0.5]]
# layer1 = reteXOR.layers[1]
# layer1.weightMatrix = [[1],[-1],[0.5]]
# print(reteXOR.calculateOutput([1,1]))
# print(reteXOR.calculateOutput([1,0]))
# print(reteXOR.calculateOutput([0,0]))
# print(reteXOR.calculateOutput([0,1]))
exit()
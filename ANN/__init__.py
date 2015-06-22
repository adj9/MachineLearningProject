import ANN.Network
from ANN.Network import *
import numpy as np
import Dataset.DatasetReader as data

__author__ = 'Daniele'

print("ciao")
name_dataset = 'Fiori.csv'

# Importazione file CSV
dataset = data.get_dataset(ANN.name_dataset)

np.random.shuffle(ANN.dataset)

# Calcolo size del dataset e divido per K sottoinsiemi
k = 10
size_dataset = int(len(ANN.dataset) / ANN.k)
#trainSet = dataset[0: 8*size_dataset]
# testSet = dataset[8*size_dataset:]
trainSet=ANN.dataset
testSet=ANN.dataset
print("TrainSet = ", ANN.trainSet)
classiOutput = set()
for esempio in ANN.trainSet:
    ANN.classiOutput.add(ANN.esempio[len(ANN.esempio)-1])

#conversione classi da insieme a lista
listaClassi = []
for c in ANN.classiOutput.copy():
    ANN.listaClassi.append(ANN.classiOutput.pop())

esempioQualsiasi = ANN.trainSet[0]
numeroInput = len(ANN.esempioQualsiasi)-1
rete = Network(ANN.numeroInput, ANN.listaClassi)
ANN.rete.addHiddenLayer(4)
ANN.rete.addOutputLayer()
ANN.rete.train(ANN.trainSet)

giuste = 0
sbagliate = 0
for test in ANN.testSet:
    outputClass = ANN.rete.classify(ANN.test[:len(ANN.test)-1])
    if (ANN.outputClass==ANN.test[len(ANN.test)-1]):
        ANN.giuste += 1
        print("<",ANN.outputClass[0:len(ANN.outputClass)-1],",",ANN.test[len(ANN.test)-1],"> OK!!!")
    else:
        ANN.sbagliate +=1
        print("<",ANN.outputClass[0:len(ANN.outputClass)-1],",",ANN.test[len(ANN.test)-1],"> SBAGLIATO!")

for lay in ANN.rete.layers:
    print(ANN.lay.weightMatrix)

print("giuste ", ANN.giuste)
print("sbagliate ", ANN.sbagliate)
print("accuracy ",float(ANN.giuste)/(ANN.giuste+ANN.sbagliate))

# reteXOR = Network(2, ["true"])
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

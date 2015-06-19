from NeuronalNetwork import Unit

__author__ = 'Alessandro'

from math import exp, pow

from NeuralNetwork.Layer import *
import NeuronalNetwork.Network
from NeuronalNetwork.Network import *
from NeuralNetwork.Input import *

def soglia(x):
    if(x < 0 ):
        result = 0
    else:
        result = 1
    return result

sigmoid = lambda x: 1 / (1 + exp(-1 * x))

sigmoid1th = lambda x: exp(x) / pow((exp(x) + 1), 2)

x1 = Input(1, [-1, -1])
x2 = Input(1, [-1, -1])

strato1 = Layer([x1, x2])
strato1.generate_matrix()

unita1 = Unit(strato1.get_weights_in(0), -1.5, soglia)
unita2 = Unit(strato1.get_weights_in(1), -0.5. soglia)

strato2 = Layer([unita1, unita2])
strato2.generate_matrix()

print(strato1.get_matrix())
#TODO Creare il secondo strato con i valori dei pesi calcolati con la funzione soglia

# lInput = Layer()
# lInput.addComponent(a11)
# lInput.addComponent(a12)
#
# #    FUNZIONA IL CASO CON if self.previous == [] - E' INUTILE INVOCARE I METODI
# #a11.setWeight()
# #a12.setWeight()
#
# a21 = Unit(0, 1, sigmoid)
#
# a21.addPrevious(a11)
# a21.addPrevious(a12)
# a21.setWeight()
#
# a22 = Unit(0, 1, sigmoid)
#
# a22.addPrevious(a11)
# a22.addPrevious(a12)
# a22.setWeight()
#
# a23 = Unit(-1, 1, sigmoid)
# a23.addPrevious(a11)
# a23.addPrevious(a12)
# a23.setWeight()
#
# lHidden = Layer()
# lHidden.addComponent(a21)
# lHidden.addComponent(a22)
# lHidden.addComponent(a23)
#
# a31 = Unit(0, 1, sigmoid)
# a31.addPrevious(a21)
# a31.addPrevious(a22)
# a31.setWeight()
#
# a32 = Unit(0, 1, sigmoid)
# a32.addPrevious(a21)
# a32.addPrevious(a22)
# a32.setWeight()
#
# a33 = Unit(-1, 1, sigmoid)
# a33.addPrevious(a21)
# a33.addPrevious(a22)
# a33.setWeight()
#
# lOutput = Layer()
# lOutput.addComponent(a31)
# lOutput.addComponent(a32)
# lOutput.addComponent(a33)
#
# print('Input:\nWeights(a11) = ', a11.getWeight(), ',   Weights(a12) = ', a12.getWeight())
# print('\nPrimo strato interno: ', 'Weights(a21) = ', a21.getWeight(), ',   Weights(a22) = ', a22.getWeight(), ' Weihts(a23) = ', a23.getWeight(), " Total weight: ", lHidden.getWeight(), '\n')
# print('\nOutout: ', 'Weights(a31) = ', a31.getWeight(), 'Weights(a32) = ', a32.getWeight(), 'Weight(a33) = ', a33.getWeight(), ' Total weight: ', lOutput.getWeight(), '\n')
#
# print('count layerIn = ', len(lInput), '\ncount HiddenLayer = ', len(lHidden), '\ncout outputLayter = ', len((lOutput)))
#
# net = Network()
# net.addLayer(lInput)
# net.addLayer(lHidden)
# net.addLayer(lOutput)
#
# weightMatrix, lines, collomns = net.generateWeightMatrix()
# print(weightMatrix)
#s = ''
#s1 = ''
#for i in range(0, lines):
#    s = '['
#    for j in range(0, collomns - 1):
#        s = s + str(weightMatrix[i][j]) + ', '
#    s1 = str(weightMatrix[i][collomns])
#    s = s + s1 + ']'
#    print(s)


from ANN.Layer import Layer

__author__ = 'Daniele'

import numpy
from numpy import zeros


class Network:
    # def funzioneSoglia(self,x):
    #     if(x>=0):
    #         return 1
    #     else:
    #         return 0
    def __init__(self, input_size, class_names, activation_function):
        super(Network, self).__init__()
        self.input_size = input_size
        self.class_names = class_names  # class_names sarà = ["Iris-setosa\n", "Iris-virginica\n", "Iris-versicolor\n"]
        self.layers = []
        self.tasso_apprendimento_alfa = 0.1# sparato a caso!!
        self.num_layers = 0
        # activation_function = math.tanh  # funzione sigmoide
        self.__activation_function = activation_function

    def addHiddenLayer(self, numNodi):
        l = []
        if self.num_layers == 0:
            l = Layer(numNodi, self.input_size, self.__activation_function)
            self.layers.append(l)
        else:
            prevLayer = self.layers[len(self.layers) - 1]
            assert isinstance(prevLayer, Layer) #verifica che prevLayer sia un Layer
            nodiPrecLayer = prevLayer.numNodes
            self.layers.append(Layer(numNodi, nodiPrecLayer, self.activation_function))
        self.num_layers += 1

        # !!!!!!!!!!!!!!!!!
        # !!!!!!!!!!!!!!
        # !!!!!!!!!!
        # self.activation_function = self.funzioneSoglia

    def addOutputLayer(self):
        prevLayer = self.layers[len(self.layers) - 1]
        assert isinstance(prevLayer, Layer)
        nodiPrecLayer = prevLayer.numNodes
        self.layers.append(Layer(len(self.class_names), nodiPrecLayer, self.__activation_function))

        self.num_layers = self.num_layers + 1

    def calculateOutput(self, input):
        outputPrevLayer = 0
        for i in range(0, self.num_layers):
            if i == 0:  # al primo layer passiamo direttamente l'input, anziché l'output del layer precedente
                self.layers[i].calculateOutput(input)
                outputPrevLayer = self.layers[i].output
            else:
                self.layers[i].calculateOutput(outputPrevLayer)
                outputPrevLayer = self.layers[i].output
        # max = 0
        # maxIndex = 0
        # for i in range(0, len(outputPrevLayer)):
        #     if (outputPrevLayer[i]>max):
        #         max = outputPrevLayer[i]
        #         maxIndex = i
        # for i in range(0, len(outputPrevLayer)):
        #     if (i==maxIndex):
        #         outputPrevLayer[i] = 1.0
        #     else:
        #         outputPrevLayer[i] = 0.0
        return outputPrevLayer

    def classify(self, input):

        networkOutput = self.calculateOutput(input)

        # l'output di calculateOutput sarà tipo [0.41, 0.98, 0.61] e andrà trasformato in Virginica/Setosa/Versicolor
        max = 0
        maxIndex = 0
        for i in range(0, len(self.class_names)):
            if (networkOutput[i] > max):
                max = networkOutput[i]
                maxIndex = i
        outputClass = self.class_names[maxIndex]
        print("netOutput: ", networkOutput, ", outputClass: ", outputClass)
        return outputClass

    def train(self, trainSet):
        # l'input sarà nella forma [attr1,attr2,attr3,attr4,CLASSE] e dovrà diventare
        # [attr1, attr2, attr3, attr4, [0,0,1]] a seconda della classe
        repeat = 0

        while (repeat < 1000):

            for esempio in trainSet:
                inputClass = esempio[len(esempio) - 1]
                classVector = [0] * len(self.class_names)  # classVector = [0,0,0,0,0]
                for i in range(0, len(self.class_names)):
                    if (inputClass == self.class_names[i]):
                        classVector[i] = 1  # ad esempio: classVector = [0,0,0,1,0]
                # esempio[len(esempio)-1] = classVector
                #
                #  ALGORITMO DI BACK PROPAGATION COME SUL LIBRO
                out = self.calculateOutput(esempio[0:len(esempio) - 1])
                diff = zeros(len(out))
                delta = zeros(len(out))
                derivative = zeros(len(out))
                outputLayer = self.layers[len(self.layers) - 1]
                for i in range(0, len(out)):
                    derivative[i] = self.derivative(self.__activation_function, outputLayer.weightedSum[i])
                    diff[i] = classVector[i] - out[i]
                    delta[i] = derivative[i] * diff[i]

                prevLayer = outputLayer
                for l in range(len(self.layers) - 2, -1, -1): #For l = L-1 a 1
                    hiddenLayer = self.layers[l]
                    oldDelta = delta
                    somma = zeros(hiddenLayer.numNodes)
                    delta = zeros(hiddenLayer.numNodes)
                    derivative = zeros(hiddenLayer.numNodes)
                    # calcolo nuova delta livello corrente
                    for j in range(0, hiddenLayer.numNodes):
                        derivative[j] = self.derivative(self.__activation_function, hiddenLayer.weightedSum[j])
                        for i in range(0, prevLayer.numNodes):
                            somma[j] += oldDelta[i] * prevLayer.weightMatrix[j][i]
                        delta[j] = derivative[j] + somma[j]
                    # aggiornamento pesi tra livello corrente e precedente
                        for i in range(0, prevLayer.numNodes):
                            #oldweight = prevLayer.weightMatrix[j][i]
                            prevLayer.weightMatrix[j][i] += self.tasso_apprendimento_alfa * hiddenLayer.output[j] * oldDelta[i]
                            #weightChange = abs(oldweight - prevLayer.weightMatrix[j][i])
                            # print("weightchange: ",weightChange)
                            # if (weightChange<self.epsilon):
                            #     pesiInvariati = pesiInvariati+1
                            # totalePesi = totalePesi + 1
                        # aggiornamento pesi bias ?????
                        #prevLayer.weightMatrix[hiddenLayer.numNodes][i] += self.tasso_apprendimento_alfa * (-1) * oldDelta[i]

                    prevLayer = hiddenLayer

                # Gestione Particolare dei collegamenti tra strato input e primo strato nascosto

                oldDelta = delta
                for j in range(0, self.input_size):
                    for i in range(0, prevLayer.numNodes):
                        #oldweight = prevLayer.weightMatrix[j][i]
                        prevLayer.weightMatrix[j][i] += self.tasso_apprendimento_alfa * float(esempio[j]) * oldDelta[i]
                        #weightChange = abs(oldweight - prevLayer.weightMatrix[j][i])
                        # print("weightchange: ",weightChange)
                        # if (weightChange<self.epsilon):
                        #     pesiInvariati = pesiInvariati+1
                        # totalePesi = totalePesi + 1
                    # aggiornamento pesi bias ?????
                    #prevLayer.weightMatrix[j + 1][i] += self.tasso_apprendimento_alfa * (-1) * oldDelta[i]
            # REPEAT?? CHECK CONVERGENZA... io direi.. per ora limitiamoci a impostare un numero di epoche prefissato
            repeat = repeat + 1

    @staticmethod
    def derivative(f, x):
        h = 1. / 1000.
        rise = f(x + h) - f(x)
        run = h
        slope = rise / run
        return slope
        # print("slope =", slope, ", f(x)*(1-f(x) =",f(x)*(1-f(x)))
        # return f(x)*(1-f(x))

        # PEZZO DI CODICE DA IMPLEMENTARE DENTRO "TRAIN"
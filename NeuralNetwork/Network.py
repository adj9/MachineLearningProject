from math import pow

from numpy import zeros

from NeuralNetwork.Layer import Layer


class Network:
    def __init__(self, input_size, class_names, activation_function):
        super(Network, self).__init__()
        self.input_size = input_size
        self.class_names = class_names  # class_names sarà = ["Iris-setosa\n", "Iris-virginica\n", "Iris-versicolor\n"]
        self.layers = []
        self.tasso_apprendimento_alfa = 0.1
        self.num_layers = 0
        self.report = open("report.txt", 'a')  # file di report apprendimento
        self.activation_function = activation_function

    def close_report(self):
        self.report.close()

    def add_hidden_layer(self, num_nodi):
        if self.num_layers == 0:
            l = Layer(num_nodi, self.input_size, self.activation_function)
            self.layers.append(l)
        else:
            prev_layer = self.layers[len(self.layers) - 1]
            assert isinstance(prev_layer, Layer)  # verifica che prev_layer sia un Layer
            nodi_prec_layer = prev_layer.numNodes
            self.layers.append(Layer(num_nodi, nodi_prec_layer, self.activation_function))
        self.num_layers += 1

    def add_output_layer(self):
        prev_layer = self.layers[len(self.layers) - 1]
        assert isinstance(prev_layer, Layer)
        nodi_prec_layer = prev_layer.numNodes
        self.layers.append(Layer(len(self.class_names), nodi_prec_layer, self.activation_function))

        self.num_layers += 1

    def calculate_output(self, input):
        output_prev_layer = 0
        for i in range(0, self.num_layers):
            if i == 0:  # Al primo layer passiamo direttamente l'input, anziché l'output del layer precedente
                self.layers[i].calculate_output(input)
                output_prev_layer = self.layers[i].output
            else:
                self.layers[i].calculate_output(output_prev_layer)
                output_prev_layer = self.layers[i].output

        return output_prev_layer

    def classify(self, input):

        network_output = self.calculate_output(input)

        # L'output di calculateOutput sarà tipo [0.41, 0.98, 0.61] e andrà trasformato in Virginica/Setosa/Versicolor
        max = 0
        max_index = 0
        for i in range(0, len(self.class_names)):
            if network_output[i] > max:
                max = network_output[i]
                max_index = i
        output_class = self.class_names[max_index]

        return output_class

    def train(self, train_set):
        # L'input sarà nella forma [attr1,attr2,attr3,attr4,CLASSE] e dovrà diventare
        # [attr1, attr2, attr3, attr4, [0,0,1]] a seconda della classe
        repeat = 0

        self.report.write(
                '\n-----------------------------------------------------------------------------------------------\n\n')
        while (repeat < 1000):

            errore_tot = 0

            for esempio in train_set:
                input_class = esempio[len(esempio) - 1]
                class_vector = [0] * len(self.class_names)
                for i in range(0, len(self.class_names)):
                    if input_class == self.class_names[i]:
                        class_vector[i] = 1

                out = self.calculate_output(esempio[0:len(esempio) - 1])
                diff = zeros(len(out))
                delta = zeros(len(out))
                derivative = zeros(len(out))
                output_layer = self.layers[len(self.layers) - 1]
                errore = 0
                for i in range(0, len(out)):
                    derivative[i] = self.derivative(self.activation_function, output_layer.weightedSum[i])
                    diff[i] = class_vector[i] - out[i]
                    delta[i] = derivative[i] * diff[i]
                    errore += pow(diff[i], 2)
                errore *= 0.5
                errore_tot += errore

                prev_layer = output_layer
                for l in range(len(self.layers) - 2, -1, -1):  # For l = L-1 a 1
                    # Inizializzazione dei dati per la back-propagation
                    hidden_layer = self.layers[l]
                    old_delta = delta
                    somma = zeros(hidden_layer.numNodes)
                    delta = zeros(hidden_layer.numNodes)
                    derivative = zeros(hidden_layer.numNodes)
                    # Calcolo nuova delta livello corrente
                    for j in range(0, hidden_layer.numNodes):
                        derivative[j] = self.derivative(self.activation_function, hidden_layer.weightedSum[j])
                        # Sommatoria sul valore dei pesi dei nodi
                        for i in range(0, prev_layer.numNodes):
                            somma[j] += old_delta[i] * prev_layer.weightMatrix[j][i]
                        delta[j] = derivative[j] + somma[j]
                        # Aggiornamento pesi tra livello corrente e precedente
                        for i in range(0, prev_layer.numNodes):
                            prev_layer.weightMatrix[j][i] += self.tasso_apprendimento_alfa * hidden_layer.output[j] * \
                                                             old_delta[i]

                    prev_layer = hidden_layer

                # Gestione Particolare dei collegamenti tra strato input e primo strato nascosto
                old_delta = delta
                for j in range(0, self.input_size):
                    for i in range(0, prev_layer.numNodes):
                        prev_layer.weightMatrix[j][i] += self.tasso_apprendimento_alfa * float(esempio[j]) * old_delta[
                            i]

            repeat += 1
            s = str('epoca: ' + str(repeat) + '     errore tot: ' + str(errore_tot / len(out)) + '\n')
            self.report.write(s)

    @staticmethod
    def derivative(f, x):
        h = 1. / 1000.
        rise = f(x + h) - f(x)
        run = h
        slope = rise / run
        return slope

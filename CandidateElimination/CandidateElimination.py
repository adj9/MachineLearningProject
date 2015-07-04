class Factors:
    factors = {}
    attributes = ()

    def __init__(self, attr):
        self.attributes = attr
        for i in attr:
            self.factors[i] = []

    def add_values(self, factor, values):
        self.factors[factor] = values


class Candidate_elimination:
    Positive = {}
    Negative = {}

    def __init__(self, data, fact, target):
        self.num_factors = len(data[0][0])
        self.factors = fact.factors
        self.attr = fact.attributes
        self.dataset = data
        self.target = target
        self.report = open("reportCandidateElimination.txt", 'a')

    def run_algo(self):
        self.report.write('###########################################################################################\n')
        self.report.write('Target: ' + self.target + '\n')
        self.report.write('###########################################################################################\n')
        G = self.initializeG()
        S = self.initializeS()
        for example in self.dataset:
            if self.is_positive(example):
                G = self.remove_inconsistent_G(G, example[0])
                S_new = S[:]
                for s in S:
                    if not self.consistent(s, example[0]):
                        S_new.remove(s)
                        generalization = self.generalize_inconsistent_S(s, example[0])
                        generalization = self.get_general(generalization, G)
                        if generalization:
                            S_new.append(generalization)
                    S = S_new[:]
                    S = self.remove_more_general(S)
            else:  # if it is negative
                S = self.remove_inconsistent_S(S, example[0])
                G_new = G[:]
                for g in G:
                    if self.consistent(g, example[0]):
                        G_new.remove(g)
                        specializations = self.specialize_inconsistent_G(g, example[0])
                        specializations = self.get_specific(specializations, S)
                        if specializations != []:
                            G_new += specializations
                    G = G_new[:]
                    G = self.remove_more_specific(G)

            self.report.write('Esempio: ' + str(example) + '\n')
            self.report.write('S: ' + str(S) + '\n')
            self.report.write('G: ' + str(G) + '\n')
            self.report.write('\n')

        self.report.write('###########################################################################################\n')
        # return [S, G]

    def initializeS(self):
        ''' Initialize the specific boundary '''
        S = tuple(['-' for factor in range(self.num_factors)])
        return [S]

    def initializeG(self):
        ''' Initialize the general boundary '''
        G = tuple(['?' for factor in range(self.num_factors)])
        return [G]

    def is_positive(self, example):
        ''' Check if a given training example is positive '''
        if example[1] == self.target:
            return True
        else:
            return False
        # else:
        #     raise TypeError("invalid target value")

    def is_negative(self, example):
        ''' Check if a given training example is negative '''
        if example[1] != self.target:
            return False
        else:
            return True
        # else:
        #     raise TypeError("invalid target value")

    def match_factor(self, value1, value2):
        ''' Check for the factors values match,
            necessary while checking the consistency of 
            training example with the hypothesis '''
        if value1 == '?' or value2 == '?':
            return True
        elif value1 == value2:
            return True
        return False

    def consistent(self, hypothesis, instance):
        ''' Check whether the instance is part of the hypothesis '''
        for i, factor in enumerate(hypothesis):
            if not self.match_factor(factor, instance[i]):
                return False
        return True

    def remove_inconsistent_G(self, hypotheses, instance):
        ''' For a positive example, the hypotheses in G
            inconsistent with it should be removed '''
        G_new = hypotheses[:]
        for g in hypotheses:
            if not self.consistent(g, instance):
                G_new.remove(g)
        return G_new

    def remove_inconsistent_S(self, hypotheses, instance):
        ''' For a negative example, the hypotheses in S
            inconsistent with it should be removed '''
        S_new = hypotheses[:]
        for s in hypotheses:
            if self.consistent(s, instance):
                S_new.remove(s)
        return S_new

    def remove_more_general(self, hypotheses):
        '''  After generalizing S for a positive example, the hypothesis in S
        general than others in S should be removed '''
        S_new = hypotheses[:]
        for old in hypotheses:
            for new in S_new:
                if old != new and self.more_general(new, old):
                    S_new.remove(new)
        return S_new

    def remove_more_specific(self, hypotheses):
        ''' After specializing G for a negative example, the hypothesis in G
        specific than others in G should be removed '''
        G_new = hypotheses[:]
        for old in hypotheses:
            for new in G_new:
                if old != new and self.more_specific(new, old):
                    G_new.remove(new)
        return G_new

    def generalize_inconsistent_S(self, hypothesis, instance):
        ''' When a inconsistent hypothesis for positive example is seen in the specific boundary S,
            it should be generalized to be consistent with the example ... we will get one hypothesis'''
        hypo = list(hypothesis)  # convert tuple to list for mutability
        for i, factor in enumerate(hypo):
            if factor == '-':
                hypo[i] = instance[i]
            elif not self.match_factor(factor, instance[i]):
                hypo[i] = '?'
        generalization = tuple(hypo)  # convert list back to tuple for immutability
        return generalization

    def specialize_inconsistent_G(self, hypothesis, instance):
        ''' When a inconsistent hypothesis for negative example is seen in the general boundary G
            should be specialized to be consistent with the example.. we will get a set of hypotheses '''
        specializations = []
        hypo = list(hypothesis)  # convert tuple to list for mutability
        for i, factor in enumerate(hypo):
            if factor == '?':
                values = self.factors[self.attr[i]]
                for j in values:
                    if instance[i] != j:
                        hyp = hypo[:]
                        hyp[i] = j
                        hyp = tuple(hyp)  # convert list back to tuple for immutability
                        specializations.append(hyp)
        return specializations

    def get_general(self, generalization, G):
        ''' Checks if there is more general hypothesis in G
            for a generalization of inconsistent hypothesis in S
            in case of positive example and returns valid generalization '''

        for g in G:
            if self.more_general(g, generalization):
                return generalization
        return None

    def get_specific(self, specializations, S):
        ''' Checks if there is more specific hypothesis in S
            for each of hypothesis in specializations of an
            inconsistent hypothesis in G in case of negative example
            and return the valid specializations'''
        valid_specializations = []
        for hypo in specializations:
            for s in S:
                if self.more_specific(s, hypo) or s == self.initializeS()[0]:
                    valid_specializations.append(hypo)
        return valid_specializations

    def exists_general(self, hypothesis, G):
        '''Used to check if there exists a more general hypothesis in
            general boundary for version space'''

        for g in G:
            if self.more_general(g, hypothesis):
                return True
        return False

    def exists_specific(self, hypothesis, S):
        '''Used to check if there exists a more specific hypothesis in
            general boundary for version space'''

        for s in S:
            if self.more_specific(s, hypothesis):
                return True
        return False

    def get_version_space(self, specific, general):
        ''' Given the specific and the general boundary of the
            version space, evaluate the version space in between '''
        while get_order(VS):
            for hypothesis in VS[:]:
                hypo = list(hypothesis)  # convert tuple to list for mutability
                for i, factor in enumerate(hypo):
                    if factor != '?':
                        hyp = hypo[:]
                        hyp[i] = '?'
                        if self.exists_general(hyp, general) and self.exists_specific(hyp, specific):
                            VS.append(tuple(hyp))

        return VS

    def get_order(self, hypothesis):
        pass

    def more_general(self, hyp1, hyp2):
        ''' Check whether hyp1 is more general than hyp2 '''
        hyp = zip(hyp1, hyp2)
        for i, j in hyp:
            if i == '?':
                continue
            elif j == '?':
                if i != '?':
                    return False
            elif i != j:
                return False
            else:  # i==j
                continue
        return True

    def more_specific(self, hyp1, hyp2):
        ''' hyp1 more specific than hyp2 is
            equivalent to hyp2 being more general than hyp1 '''
        return self.more_general(hyp2, hyp1)

#
# --------------------------------------------------------------------------------------------------------------------
#                                       Fine scatola chiusa
# --------------------------------------------------------------------------------------------------------------------
#

num_bin = 10
import copy

def count_bin(dataset, position):

    new_dataset = copy.deepcopy(dataset)
    x = list(zip(*dataset))[position]
    x = [float(i) for i in x]
    min_x = min(x)
    max_x = max(x)
    grandezza_bin = (max_x - min_x) / num_bin

    for i in range(len(dataset)):
        start_bin = min_x
        for j in range(1, num_bin + 1):
            end_bin = min_x + grandezza_bin * j

            if (j < num_bin) & (float(dataset[i][position]) >= start_bin) & (float(dataset[i][position]) < end_bin):
                new_dataset[i][position] = "bin"+str(j)
            elif (float(dataset[i][position]) >= start_bin) & (float(dataset[i][position]) <= end_bin):
                new_dataset[i][position] = "bin"+str(j)

            start_bin = end_bin

    return new_dataset

def modifica_dataset(dataset):

    new_dataset = list()
    new_list = [0, 0]

    for i in dataset:
        new_list[0] = (i[0], i[1], i[2], i[3])
        new_list[1] = i[4]
        new_dataset.append(new_list)
        new_list = [0, 0]

    return new_dataset

def candidate(dataset_train, dataset_test):
    for i in range(0, 4):
        dataset_train = count_bin(dataset_train, i)
    # print(dataset_train)
    attributes = ('x1', 'x2', 'x3', 'x4')
    f = Factors(attributes)
    f.add_values('x1', ('bin1', 'bin2', 'bin3', 'bin4', 'bin5', 'bin6', 'bin7', 'bin8', 'bin9', 'bin10'))
    f.add_values('x2', ('bin1', 'bin2', 'bin3', 'bin4', 'bin5', 'bin6', 'bin7', 'bin8', 'bin9', 'bin10'))
    f.add_values('x3', ('bin1', 'bin2', 'bin3', 'bin4', 'bin5', 'bin6', 'bin7', 'bin8', 'bin9', 'bin10'))
    f.add_values('x4', ('bin1', 'bin2', 'bin3', 'bin4', 'bin5', 'bin6', 'bin7', 'bin8', 'bin9', 'bin10'))

    # Settiamo il nuovo dataset
    dataset = modifica_dataset(dataset_train)

    # Richiamo tre volte il candidate elimination passandogli i tre diversi valori di target
    a = Candidate_elimination(dataset, f, "Iris-setosa")
    a.run_algo()
    b = Candidate_elimination(dataset, f, "Iris-versicolor")
    b.run_algo()
    c = Candidate_elimination(dataset, f, "Iris-virginica")
    c.run_algo()

#
# dataset=[[('sunny','warm','normal','strong','warm','same'),'Y'],[('sunny','warm','high','strong','warm','same'),'Y'],[('rainy','cold','high','strong','warm','change'),'N'],[('sunny','warm','high','strong','cool','change'),'Y']]
# attributes =('Sky','Temp','Humidity','Wind','Water','Forecast')
# f = Factors(attributes)
# f.add_values('Sky',('sunny','rainy','cloudy'))
# f.add_values('Temp',('cold','warm'))
# f.add_values('Humidity',('normal','high'))
# f.add_values('Wind',('weak','strong'))
# f.add_values('Water',('warm','cold'))
# f.add_values('Forecast',('same','change'))
# a = Candidate_elimination(dataset,f)
# a.run_algo()
# print a.specialize_inconsistent_G(('?','?','?','?','?','?'),('rainy','cold','high','strong','warm','change'))
# print a.generalize_inconsistent_S(('-','-','-','-','-','-'),('sunny','warm','normal','strong','warm','same'))
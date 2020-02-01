from copy import deepcopy
import numpy

from nn import *
from Mutation import *

class ML:
    def __init__(self, template, amount):
        self.template = template
        self.amount = amount
        self.nns = []
        self.bests = []
    
    def init(self):
        self.template.init()

        for i in range(0, self.amount):
            nn = deepcopy(self.template)
            self.nns.append(nn)

    def randomize(self):
        for nn in self.nns: nn.randomize()
    
    def clone(self, template):
        for i in range(0, self.amount):
            self.nns[i] = deepcopy(template)

    def cloneBest(self):
        template = self.best()
        self.clone(template)
    
    def best(self):
        return self.bests[-1]
    
    def mutate(self):
        for i in range(0, self.amount):
            f = i / self.amount
            mutate(self.nns[i], f)

    def test(self, test):
        scores = []

        for nn in self.nns:
            score = test.test(nn)
            scores.append(score)

        lowest = numpy.argmin(scores)

        nn = self.nns[lowest]

        self.bests.append(nn)
        return nn

class Test:
    def test(self, nn):
        return 0
import copy
import numpy

from nn import *
from ml import *
from ActivationFunction import *

class AddTest(Test):
    def test(self, nn):
        score = 0

        for a in range(1, 10):
            for b in range(1, 10):
                c = 2 * a + b

                nn.setnode(0, a)
                nn.setnode(1, b)

                x = nn.generatenode(0)

                score += abs(c - x)

        return score

ac = Linear()

layers = [ ]
layers.append(Layer(None, 2, ac))
layers.append(Layer(layers[0], 1, ac))

template = NN(layers)

ml = ML(template, 50)
ml.init()
ml.randomize()

test = AddTest()

best = None

for i in range(0, 100):
    best = ml.test(test)
    ml.clone(best)
    ml.mutate()

    best.setnode(0, 3)
    best.setnode(1, 6)
    print (best.generatenode(0))
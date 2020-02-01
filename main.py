from nn import *
from ActivationFunction import *

ac = Relu()

layers = [ ]
layers.append(Layer(None, 2, ac))
layers.append(Layer(layers[0], 1, ac))

nn = NN(layers)
nn.init()

nn.layers[1].nodes[0].weighes[0] = 2
nn.layers[1].nodes[0].weighes[1] = 1

nn.setnode(0, 3)
nn.setnode(1, 6)

x = nn.generate()

print (x)
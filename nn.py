from random import *

class NN:
    def __init__(self, layers):
        self.layerCount = len(layers)
        self.layers = layers

    def init(self):
        for layer in self.layers: layer.init()

    def randomize(self):
        for layer in self.layers: layer.randomize()

    def setnode(self, node, value):
        self.layers[0].nodes[node].value = value

    def getnode(self, node):
        return self.layers[self.layerCount - 1].nodes[node].value

    def generatenode(self, node):
        return self.layers[self.layerCount - 1].nodes[node].generate()

    def generate(self):
        x = []
        for node in self.layers[self.layerCount - 1].nodes:
            x.append(node.generate())
        return x
    

class Layer:
    def __init__(self, previouseLayer, nodeCount, activationFunction):
        self.previouseLayer = previouseLayer
        self.nodeCount = nodeCount
        self.nodes = []
        self.activationFunction = activationFunction
    
    def init(self):
        for i in range(0, self.nodeCount):
            node = Node(self)
            node.init()
            self.nodes.append(node)

    def randomize(self):
        for node in self.nodes: node.randomize()



class Node:
    def __init__(self, layer):
        self.layer = layer

        self.value = 0
        self.weighes = []
        self.bias = 0

    def init(self):
        if not self.isInput(): self.initWeighes()
        

    def initWeighes(self):
        for i in range(0, self.layer.previouseLayer.nodeCount):
            self.weighes.append(0)

    def randomize(self):
        if not self.isInput():
            for i in range(0, len(self.weighes)): self.weighes[i] = random() * 2 - 1
        self.bias = random() * 2 - 1

    def isInput(self):
        return self.layer.previouseLayer == None

    def generate(self):
        if self.isInput():
            return self.value

        value = self.bias
        for i in range(0, len(self.layer.previouseLayer.nodes)):
            value += self.layer.previouseLayer.nodes[i].generate() * self.weighes[i]

        value = self.layer.activationFunction.parse(value)

        return value


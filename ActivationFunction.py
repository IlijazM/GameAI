import math

class ActivationFunction:
    def parse(self, value):
        return value

class Linear(ActivationFunction):
    def parse(self, value):
        return value

class Relu(ActivationFunction):
    def parse(self, value):
        if value > 0: return value
        return 0

class Sigmoid(ActivationFunction):
    def parse(self, value):
        x = 2 / (math.e ** -value + 1) - 1
        return x
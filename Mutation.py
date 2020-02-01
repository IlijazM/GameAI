import math

from nn import *

def mutate(nn, amount):
    indexes = []

    for i in range(0, len(nn.layers)):
        for j in range(0, len(nn.layers[i].nodes)):
            indexes.append([i, j, -1])
            for k in range(0, len(nn.layers[i].nodes[j].weighes)):
                indexes.append([i, j, k])

    randomCounts = len(indexes) - round(len(indexes) * amount)
    
    for i in range(0, randomCounts):
        index = math.floor(random() * len(indexes))
        indexes.pop(index)
    
    for index in indexes:
        i = index[0]
        j = index[1]
        k = index[2]

        r = random() * 2 - 1

        if k == -1:
            nn.layers[i].nodes[j].bias += r
        else:
            nn.layers[i].nodes[j].weighes[k] += r
        
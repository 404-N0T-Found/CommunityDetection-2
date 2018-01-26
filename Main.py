# https://arxiv.org/pdf/0709.2938.pdf

from collections import Counter
from random import shuffle


def initialize():
    rndOrder = []
    graph = []
    dict = {}
    with open("YpInteraction.txt") as f:
        for line in f:
            dict.update({line.strip('\n').split()[0]: 0})
            dict.update({line.strip('\n').split()[1]: 0})
            graph.append([line.strip('\n').split()[0], line.strip('\n').split()[1]])
    lbl = 0
    for item in dict.items():
        rndOrder.append([item[0], [lbl]])
        lbl += 1
    shuffle(rndOrder)
    return rndOrder,graph


def arrangeNodesOrder():
    return


def labelPropagate():
    return


if __name__ == '__main__':
    # step1
    graph = initialize()

    t = 1

    arrangeNodesOrder()

    labelPropagate()

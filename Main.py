# https://arxiv.org/pdf/0709.2938.pdf

from collections import Counter


def initialize():
    graph = []
    dict = {}
    with open("YpInteraction.txt") as f:
        for line in f:
            dict.update({line.strip('\n').split()[0]: 0})
            dict.update({line.strip('\n').split()[1]: 0})
    lbl = 0
    for item in dict.items():
        graph.append([item[0], [lbl]])
        lbl += 1
    return graph


def arrangeNodesOrder():
    return


def labelPropagate():
    return


if __name__ == '__main__':
    initialize()
    t = 1
    arrangeNodesOrder()
    labelPropagate()

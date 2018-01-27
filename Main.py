# https://arxiv.org/pdf/0709.2938.pdf
from collections import Counter
from random import shuffle
from random import randint


# This function Read File and Add nodes to dictinary(distinct)
#
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
    return rndOrder, graph


# node i in the whole graph
def findNeighbours(node, graph):
    lst = []
    for item in graph:
        if item[0] == node:
            lst.append(item)
    return lst


def getNeighboursLabels(lstNei, nodesLabels):
    lstlbls = []
    for item in nodesLabels:
        for neig in lstNei:
            if neig[1] == item[0]:
                lstlbls.append(item[1][-1])

    return lstlbls


def getNodeLabel(labels):
    countlbls = Counter(labels)
    canSetedlbl = [countlbls[i] for i in countlbls if countlbls[i] > 1]
    if (len(canSetedlbl) > 0):
        rnd = randint(0, len(canSetedlbl) - 1)
        return canSetedlbl[rnd]
    else:
        return


def getDominantLabel(lst):
    lbls = [lst[i] for i in range(len(lst))]
    return lbls


def labelPropagate(nodesorder, graph):
    i = 0
    while (1):
        for item in nodesorder:
            neighbors = findNeighbours(item[0])
            neig_lbls = getNeighboursLabels(neighbors, nodesorder)
        nodesorder = shuffle(nodesorder)
    return


if __name__ == '__main__':
    # step1
    rndOrder, graph = initialize()
    t = 1

    labelPropagate(rndOrder, graph)

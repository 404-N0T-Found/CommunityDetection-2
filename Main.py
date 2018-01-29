# https://arxiv.org/pdf/0709.2938.pdf
from collections import Counter
from random import shuffle
from random import randint

graph = []


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


def checkResult(node):
    for item in graph:
        if item[0] == node:
            print(item)
        elif item[1] == node:
            print(item)


# node i in the whole graph
def findNeighbours(node):
    lst = []
    for item in graph:
        if item[0] == node:
            lst.append(item[1])
        elif item[1] == node:
            lst.append(item[0])
    myset = set(lst)
    return list(myset)


def getNeighboursLabels(lstNei, nodesLabels):
    lstlbls = []
    for item in nodesLabels:
        for neig in lstNei:
            if neig == item[0]:
                lstlbls.append(item[1][-1])
    return lstlbls


def checkHasMaximumLabel(lbls, nodelbl):
    myset = set(lbls)
    mylst = [lbls.count(i) for i in myset]
    myset = list(myset)
    m = lbls.count(nodelbl)
    lbl = [myset[i] for i, j in enumerate(mylst) if j <= m]

    if len(lbl) == len(myset):
        return True
    return False


def getNodeLabel(labels):
    # if len(labels) == 0:
    #     return -1
    myset = set(labels)
    mylst = [labels.count(i) for i in myset]
    myset = list(myset)
    m = max(mylst)
    lbl = [myset[i] for i, j in enumerate(mylst) if j == m]

    return lbl[randint(0, len(lbl) - 1)]


    # countlbls = Counter(labels)
    # canSetedlbl = [countlbls[i] for i in countlbls if countlbls[i] > 1]
    #
    # if (len(canSetedlbl) > 1):
    #     rnd = randint(0, len(canSetedlbl) - 1)
    #     return canSetedlbl[rnd]
    # elif len(canSetedlbl) == 1:
    #     return canSetedlbl[0]
    # else:
    #     rnd = randint(0, len(labels) - 1)
    #     return labels[rnd]


def generateJson():
    return


def stopPropagate(nodesOrder):
    for i in range(len(nodesOrder)):
        # checkResult(nodesOrder[i][0])
        neighbors = findNeighbours(nodesOrder[i][0])
        neig_lbls = getNeighboursLabels(neighbors, nodesOrder)
        nodelbl = getNodeLabel(neig_lbls)
        if checkHasMaximumLabel(neig_lbls, nodelbl) == True:
            return True
    return False


def labelPropagate(nodesorder):
    while (1):
        stopCount = 0
        for i in range(len(nodesorder)):
            # checkResult(nodesorder[i][0])
            neighbors = findNeighbours(nodesorder[i][0])
            neig_lbls = getNeighboursLabels(neighbors, nodesorder)
            nodelbl = getNodeLabel(neig_lbls)

            # if nodelbl != -1:
            nodesorder[i][1].append(nodelbl)
            # else:
            #     nodesorder[i][1].append(nodesorder[i][1][-1])
            print(nodesorder[i])
        # if stopCount == len(nodesorder):
        #     break
        # if stopCount > 0:
        #     break
        if stopPropagate(nodesorder) == True:
            break
        print(nodesorder)
        shuffle(nodesorder)
        print(nodesorder)
    return


if __name__ == '__main__':
    # step1
    rndOrder, graph = initialize()
    t = 1

    labelPropagate(rndOrder)

# https://arxiv.org/pdf/0709.2938.pdf

from collections import Counter


def initialize():
    graph = {}
    dict = {}
    with open("YpInteraction.txt") as f:
        for line in f:
            dict.update({line.strip('\n').split()[0]: 0})
            dict.update({line.strip('\n').split()[1]: 0})
            # graph.append((line.split()[0], line.split()[1]))
    # graph.sort(key=lambda x: x[0])
    # print(graph)

    # https://stackoverflow.com/questions/16013485/counting-the-amount-of-occurrences-in-a-list-of-tuples
    # print(Counter(elem[0] for elem in graph))
    # print(Counter(elem[1] for elem in graph))
    print(dict, len(dict))
    return graph


def arrangeNodesOrder():
    return


def labelPropagate():
    return


if __name__ == '__main__':
    # print('Hi')
    # loadData()
    initialize()
    t = 1
    arrangeNodesOrder()
    labelPropagate()

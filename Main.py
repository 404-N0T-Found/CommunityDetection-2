#https://arxiv.org/pdf/0709.2938.pdf
from collections import Counter


def loadData():
    graph=[]
    with open("YpInteraction(new).txt") as f:
        for line in f:
            graph.append((line.split()[0], line.split()[1]))
    graph.sort(key=lambda x: x[0])
    print(graph)

    # https://stackoverflow.com/questions/16013485/counting-the-amount-of-occurrences-in-a-list-of-tuples
    print(Counter(elem[0] for elem in graph))
    print(Counter(elem[1] for elem in graph))
    return graph
def initialize():
    return "Order"

def arrangeNodesOrder():
    return

if __name__ == '__main__':
    print('Hi')
    loadData()
    initialize()
    t=1
    arrangeNodesOrder()

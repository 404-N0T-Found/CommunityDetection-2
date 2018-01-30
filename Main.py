# initial Network(make graph, initiate labels)
# find label For node i base Neighbours
# check Condition
from random import shuffle

graph = {}


def initial():
    graph = {}
    with open('YpInteraction.txt') as file:
        for line in file:
            node1, node2 = line.strip('\n').split()
            if node1 not in graph:
                graph[node1] = {'neighbours': []}
            if node2 not in graph:
                graph[node2] = {'neighbours': []}
            graph[node1]['neighbours'].append(graph[node2])
            graph[node2]['neighbours'].append(graph[node1])

    label = 0
    for item in graph:
        graph[item]['label'] = label
        label += 1
    return graph


def getNeighbNodeLabels(item):
    return [neighbor['label'] for neighbor in item]


def getNodeLabel(labels):
    shuffle(labels)
    lbl = max(labels, key=labels.count)
    return lbl


def checkCondition(labels, nodelbl):
    lbl = max(labels, key=labels.count)
    return labels.count(lbl) == labels.count(nodelbl)


def checkStopCondition():
    for item in graph:
        neighblbls = getNeighbNodeLabels(graph[item]['neighbours'])

        result = checkCondition(neighblbls, graph[item]['label'])
        if result == False:
            return False
    return True


def generateJson():
    return 1


def displayComm():
    lstlbl = []
    for item in graph:
        lstlbl.append(graph[item]["label"])
    mycomm = set(lstlbl)
    memcnt = [lstlbl.count(i) for i in mycomm]
    mycomm=list(mycomm)
    print("Communities count is " + str(len(mycomm)))
    for i in range(len(mycomm)):
        print("Community "+ str(mycomm[i])+" has a "+str(memcnt[i])+"member!")


def labelPropagate():
    keys = list(graph.keys())
    while True:
        shuffle(keys)
        for key in keys:
            NeigbLabels = getNeighbNodeLabels(graph[key]['neighbours'])
            graph[key]['label'] = getNodeLabel(NeigbLabels)
        if checkStopCondition():
            break
    displayComm()


if __name__ == '__main__':
    graph = initial()

    labelPropagate()

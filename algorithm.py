import math
import random
import copy

def karger(G, k):
    min = math.inf
    for i in range(0, k):
        t = full_contraction(copy.deepcopy(G))
        if t < min:
            min = t
    return min

def full_contraction(G):
    nodes = len(G.V)
    next_node = nodes + 1
    for i in range(0, nodes - 2):
        e = random.choice(G.E)
        v1 = e[0]
        v2 = e[1]
        contraction(G, v1, v2, next_node)
        next_node += 1
    return len(G.E)

def contraction(G, v1, v2, next_node):

    for edge in G.E:
        if edge[0] == v1 and edge[1] == v2:
            G.E.remove([v1, v2])
        elif edge[0] == v2 and edge[1] == v1:
            G.E.remove([v2, v1])

    for i in range (0, len(G.E)):
        if G.E[i][0] == v1 or G.E[i][0] == v2:
            G.E[i][0] = next_node
        if G.E[i][1] == v1 or G.E[i][1] == v2:
            G.E[i][1] = next_node

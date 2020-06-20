import math
import random
import copy

def Karger(G, k):
    min = math.inf
    for i in range(0, k):
        t = full_contraction(G)
        if t < min:
            min = t
    return min

def full_contraction(G):
    G = copy.copy(G)

    next_node = len(G.V) + 1
    for i in range(0, len(G.V)-2):
        e = random.choice(G.E)
        v1 = e[0]
        v2 = e[1]
        contraction(G, v1, v2, next_node)
        next_node += 1
    return len(G.V)

def contraction(G, v1, v2, next_node):
    G.V.remove(v1)
    G.V.remove(v2)
    G.E.remove([v1, v2])
    G.E.remove([v2, v1])

    for edge in G.E:
        if edge[0] == v1 or edge[0] == v2:
            edge[0] = next_node
        if edge[1] == v1 or edge[1] == v2:
            edge[1] = next_node

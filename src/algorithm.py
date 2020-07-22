import math
import time
import random
import statistics
import copy


def karger(G, k, expected_minimum, timeout):
    # this stuff is needed to time the algorithm
    beginning_total = time.time()
    contraction_times = []          # i'll be returning the mean execution time of full_contraction
    found_flag = False              # this is needed to get the discovery_time
    discovery_time = math.inf

    minimum = math.inf
    for i in range(0, k):
        # timing each contraction, calculating mean in the end
        beginning_contraction = time.time()
        t = full_contraction(copy.deepcopy(G))
        ending_contraction = time.time()

        contraction_times.append(abs(ending_contraction-beginning_contraction))

        # exit if timeout reached
        if time.time() - beginning_total >= timeout:
            ending_total = time.time()
            total_time = abs(ending_total - beginning_total)
            print('actual k {}'.format(i))
            return minimum, statistics.mean(contraction_times), total_time, discovery_time, minimum - expected_minimum

        if t < minimum:
            minimum = t
        # needed to find discovery_time
        if t <= expected_minimum and not found_flag:
            discovery_time = abs(time.time()-beginning_total)
            found_flag = True

    ending_total = time.time()
    total_time = abs(ending_total-beginning_total)
    return minimum, statistics.mean(contraction_times), total_time, discovery_time, (minimum-expected_minimum)/expected_minimum


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
    G.E[:] = [e for e in G.E if e != [v1, v2] and e != [v2,v1]]

    for i in range (0, len(G.E)):
        if G.E[i][0] == v1 or G.E[i][0] == v2:
            G.E[i][0] = next_node
        if G.E[i][1] == v1 or G.E[i][1] == v2:
            G.E[i][1] = next_node

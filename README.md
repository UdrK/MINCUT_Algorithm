# MINCUT_Algorithm

As exercise for the advanced algorithms class i'm taking, i need to implement Karger's algorithm that given a graph returns a minimum cut.

The language i've choosen for this exercise is python, the decision is based on the fact that the exercise is thought for groups of 3 students but i've decided to do it on my own, and i prefer speed of development over performances.

The graphs to be used for testing are in the **mincut_dataset** folder.

## What is a mincut?

Let a graph G be a couple (V, E) where V is a set of vertices and E is a set of edges, where each edge is a triplet (u, v, w) where u and v are vertices and w is an integer representing the weight of the edge between u and v.

A cut M is a partition of V in two disjoint sets (S, T), a cutset instead, is the set of edges such that start in S and end in T. The size of a cut is the cardinality of the cutset. 

Then, the mincut is the cut of smallest size.

## Results:

The biggest result: **python is slow**.

Compared to implementations in other languages python's execution time is orders of magnitude bigger.

The second biggest result: **The discovery time is much smaller than the execution time**.

Karger's algorithm is a probabilistic algorithm: it works by repeating a procedure that is unlikely to find the optimal solution, but by repeating it this probability stacks and you end up with the optimal solution. The number of repetitions is defined based on the probability of success of the procedure, however karger's algorithm finds the optimal solution a lot sooner.

Complete results in report.pdf.

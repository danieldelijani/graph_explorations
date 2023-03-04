I chose to represent graphs similar to a streaming algorithm, as simply a list of tuples where each tuple (v1, v2) represents the existance of an edge v1 <-> v2. I chose this because it works very well with the algorithms for graph exploration, as algorithm1 has a list of edges as the sole parameter, and the rest of the algorithms have an edge as their parameter.

I have listed the files associated with each problem, as well as the written answers to any questions below.

1. problem_1.py. For my own algorithm, I store already computed values for each edge. So, if we already know an edge was visited we don't have to do the computation again. I do this by using an LRU Cache.
2. 
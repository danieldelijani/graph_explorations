I chose to represent graphs similar to a streaming algorithm, as simply a list of tuples where each tuple (v1, v2) represents the existance of an edge v1 <-> v2. I chose this because it works very well with the algorithms for graph exploration, as algorithm1 has a list of edges as the sole parameter, and the rest of the algorithms have an edge as their parameter.

I have listed the files associated with each problem, the written answers to any questions, and other notes below.

1. problem_1.py. For my own algorithm, I store already computed values for each edge. So, if we already know an edge was visited we don't have to do the computation again. I do this by using an LRU Cache.
2. problem_2.py. generate_graph_1 is the graph generation algorithm suggested in 2b. generate_graph_2 is the [Erdős-Rényi model for generating random graphs](https://www.geeksforgeeks.org/erdos-renyl-model-generating-random-graphs/).
3. problem_3.py, problem_3_table.csv, effect_of_d_on_num_recursive_calls.png
4. problem_4.py, problem_4_table.csv, effect_of_d_and_graph_generation_algorithm_on_num_recursive_calls.png
5. algorithm2 generate_graph_1 -> This looks to be an exponential function.
algorithm2 generate_graph_2 -> This looks to be an exponential function.
algorithm3 generate_graph_1 -> This looks to be an exponential function.
algorithm3 generate_graph_2 -> This looks to be an exponential function.
algorithm4 generate_graph_1 -> This looks to be a polynomial function.
algorithm4 generate_graph_2 -> This looks to be a polynomial function.
algorithm5 generate_graph_1 -> This looks to be a linear function.
algorithm5 generate_graph_2 -> This looks to be a linear function.
One interesting insight is that it seems as though each algorithm is strictly reduced time complexity from the previous algorithm.
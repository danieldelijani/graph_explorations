import matplotlib.pyplot as plt
import pandas as pd

from problem_1 import *
from problem_2 import generate_graph_1, generate_graph_2
import pandas as pd
from tqdm import tqdm

def average(lst):
    """Returns average value of a list of numbers."""
    return sum(lst) / len(lst)

if __name__ == '__main__':
    num_verticies = 1000
    maximum_d_value = 5
    d_values = []
    algo_2_generate_graph_1_recurive_calls_over_d = []
    algo_3_generate_graph_1_recurive_calls_over_d = []
    algo_4_generate_graph_1_recurive_calls_over_d = []
    algo_5_generate_graph_1_recurive_calls_over_d = []

    algo_2_generate_graph_2_recurive_calls_over_d = []
    algo_3_generate_graph_2_recurive_calls_over_d = []
    algo_4_generate_graph_2_recurive_calls_over_d = []
    algo_5_generate_graph_2_recurive_calls_over_d = []

    for d in range(1, maximum_d_value+1, 1):
        algo_2_generate_graph_1_recursives = []
        algo_3_generate_graph_1_recursives = []
        algo_4_generate_graph_1_recursives = []
        algo_5_generate_graph_1_recursives = []

        algo_2_generate_graph_2_recursives = []
        algo_3_generate_graph_2_recursives = []
        algo_4_generate_graph_2_recursives = []
        algo_5_generate_graph_2_recursives = []

        for _ in tqdm(range(2)):
            edges_1 = generate_graph_1(num_verticies, d)
            algo_2_generate_graph_1_recursives.append(algorithm2(edges_1)[1])
            algo_3_generate_graph_1_recursives.append(algorithm3(edges_1)[1])
            algo_4_generate_graph_1_recursives.append(algorithm4(edges_1)[1])
            algo_5_generate_graph_1_recursives.append(algorithm5(edges_1)[1])

            edges_2 = generate_graph_2(num_verticies, d)
            algo_2_generate_graph_2_recursives.append(algorithm2(edges_2)[1])
            algo_3_generate_graph_2_recursives.append(algorithm3(edges_2)[1])
            algo_4_generate_graph_2_recursives.append(algorithm4(edges_2)[1])
            algo_5_generate_graph_2_recursives.append(algorithm5(edges_2)[1])

        algo_2_generate_graph_1_recurive_calls_over_d.append(average(algo_2_generate_graph_1_recursives))
        algo_3_generate_graph_1_recurive_calls_over_d.append(average(algo_3_generate_graph_1_recursives))
        algo_4_generate_graph_1_recurive_calls_over_d.append(average(algo_4_generate_graph_1_recursives))
        algo_5_generate_graph_1_recurive_calls_over_d.append(average(algo_5_generate_graph_1_recursives))
        
        algo_2_generate_graph_2_recurive_calls_over_d.append(average(algo_2_generate_graph_2_recursives))
        algo_3_generate_graph_2_recurive_calls_over_d.append(average(algo_3_generate_graph_2_recursives))
        algo_4_generate_graph_2_recurive_calls_over_d.append(average(algo_4_generate_graph_2_recursives))
        algo_5_generate_graph_2_recurive_calls_over_d.append(average(algo_5_generate_graph_2_recursives))
        
        d_values.append(d)

    df = pd.DataFrame({
    'd': d_values,
    'algorithm2 generate_graph_1': algo_2_generate_graph_1_recurive_calls_over_d,
    'algorithm3 generate_graph_1': algo_3_generate_graph_1_recurive_calls_over_d,
    'algorithm4 generate_graph_1': algo_4_generate_graph_1_recurive_calls_over_d,
    'algorithm5 generate_graph_1': algo_5_generate_graph_1_recurive_calls_over_d,
    'algorithm2 generate_graph_2': algo_2_generate_graph_2_recurive_calls_over_d,
    'algorithm3 generate_graph_2': algo_3_generate_graph_2_recurive_calls_over_d,
    'algorithm4 generate_graph_2': algo_4_generate_graph_2_recurive_calls_over_d,
    'algorithm5 generate_graph_2': algo_5_generate_graph_2_recurive_calls_over_d
    })
    
    df.to_csv('problem_4_table.csv', index=False)

    plt.plot(d_values, algo_2_generate_graph_1_recurive_calls_over_d, label='algorithm2 generate_graph_1')
    plt.plot(d_values, algo_3_generate_graph_1_recurive_calls_over_d, label='algorithm3 generate_graph_1')
    plt.plot(d_values, algo_4_generate_graph_1_recurive_calls_over_d, label='algorithm4 generate_graph_1')
    plt.plot(d_values, algo_5_generate_graph_1_recurive_calls_over_d, label='algorithm5 generate_graph_1')
    
    plt.plot(d_values, algo_2_generate_graph_2_recurive_calls_over_d, label='algorithm2 generate_graph_2')
    plt.plot(d_values, algo_3_generate_graph_2_recurive_calls_over_d, label='algorithm3 generate_graph_2')
    plt.plot(d_values, algo_4_generate_graph_2_recurive_calls_over_d, label='algorithm4 generate_graph_2')
    plt.plot(d_values, algo_5_generate_graph_2_recurive_calls_over_d, label='algorithm5 generate_graph_2')

    plt.legend()
    plt.title('Effect of d and Graph Generation Algorithm on Number of Recurive Calls for Each Algorithm')
    plt.xlabel('d')
    plt.ylabel('Number of Recursive Calls')
    plt.savefig('effect_of_d_and_graph_generation_algorithm_on_num_recursive_calls.png')

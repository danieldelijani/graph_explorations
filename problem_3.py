from problem_1 import *
from problem_2 import generate_graph_1
import pandas as pd
from tqdm import tqdm

def average(lst):
    """Returns average value of a list of numbers."""
    return sum(lst) / len(lst)

if __name__ == '__main__':
    num_verticies = 100
    maximum_d_value = 5
    d_values = []
    algo_2_recurive_calls_over_d = []
    algo_3_recurive_calls_over_d = []
    algo_4_recurive_calls_over_d = []
    algo_5_recurive_calls_over_d = []

    for d in range(1, maximum_d_value, 1):
        algo_2_recursives = []
        algo_3_recursives = []
        algo_4_recursives = []
        algo_5_recursives = []

        for _ in tqdm(range(3)):
            edges = generate_graph_1(num_verticies, d)
            algo_2_recursives.append(algorithm2(edges)[1])
            algo_3_recursives.append(algorithm3(edges)[1])
            algo_4_recursives.append(algorithm4(edges)[1])
            algo_5_recursives.append(algorithm5(edges)[1])

        algo_2_recurive_calls_over_d.append(average(algo_2_recursives))
        algo_3_recurive_calls_over_d.append(average(algo_3_recursives))
        algo_4_recurive_calls_over_d.append(average(algo_4_recursives))
        algo_5_recurive_calls_over_d.append(average(algo_5_recursives))
        d_values.append(d)

    df = pd.DataFrame({
        'd': d_values,
        'algorithm2': algo_2_recurive_calls_over_d,
        'algorithm3': algo_3_recurive_calls_over_d,
        'algorithm4': algo_4_recurive_calls_over_d,
        'algorithm5': algo_5_recurive_calls_over_d
        })
    
    df.to_csv('problem_3_table.csv', index=False)
        

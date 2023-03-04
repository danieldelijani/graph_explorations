import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('problem_3_table.csv')
    plt.plot(df['d'], df['algorithm2'], label='algorithm2')
    plt.plot(df['d'], df['algorithm3'], label='algorithm3')
    plt.plot(df['d'], df['algorithm4'], label='algorithm4')
    plt.plot(df['d'], df['algorithm5'], label='algorithm5')
    plt.legend()
    plt.title('Effect of d on Number of Recurive Calls for Each Algorithm')
    plt.xlabel('d')
    plt.ylabel('Number of Recursive Calls')
    plt.savefig('effect_of_d_on_num_recursive_calls.png')

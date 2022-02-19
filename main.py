import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import partial
from mpl_toolkits.mplot3d import Axes3D
import time

q_95 = partial(pd.Series.quantile, q=0.95)
q_95.__name__ = "95%"

q_99 = partial(pd.Series.quantile, q=0.99)
q_99.__name__ = "99%"

def main(data):
    df = pd.DataFrame(data)
    df = df[sorted(df.columns)]
    # df.to_csv("data.csv", mode="a", index=False)
    df.to_csv("data.csv", mode="a", index=False, header=False)
    df = pd.read_csv("data.csv")
    expected = pd.DataFrame({
                                "1": [3.841, 6.635],
                                "2": [5.991, 9.210],
                                "3": [7.815, 11.34],
                                "4": [9.488, 13.28],
                                "5": [11.07, 15.09],
                                "6": [12.59, 16.81],
                                "7": [14.07, 18.48],
                                "8": [15.51, 20.09],
                                "9": [16.92, 21.67],
                                "10":[18.31, 23.21]
                            },
                            index=['95%', '99%'])

    # Show 95th and 99th quantile
    table = df.agg([q_95, q_99])
    print(table)

    # Show difference from expected
    print("\nDifference: \n")
    print(table.subtract(expected).abs())

    # Display graphs
    # df.plot.hist(subplots=True, bins=20)
    # plt.show()

    # Write to file
    with open("README.md", "w") as file:
        file.write("# Chi Square\n\n")
        file.write(table.to_markdown())
        file.write("\n## Difference from actual values\n\n")
        file.write(table.subtract(expected).abs().to_markdown())

def accuracy(data):
    expected = pd.DataFrame({
                                1: [3.841, 6.635],
                                2: [5.991, 9.210],
                                3: [7.815, 11.34],
                                4: [9.488, 13.28],
                                5: [11.07, 15.09],
                            },
                            index=['95%', '99%'])

    # TODO: This is slow
    results = {}
    for x in data:
        results[x] = []
        for j in data[x]:
            df = pd.DataFrame(j)
            df = df[sorted(df.columns)]
            table = df.agg([q_95, q_99]).subtract(expected).abs()
            results[x].append(table.mean().mean())
    results = pd.DataFrame(results).mean()
    localtime = time.localtime(time.time())
    print("Python finished: %d:%d:%d" %(localtime.tm_hour,localtime.tm_min,localtime.tm_sec))
    print(results)
    sets, reps = zip(*results.index)
    ax = plt.figure().add_subplot(projection='3d')
    ax.scatter(sets, reps, results.values)
    ax.set_xlabel('Sets')
    ax.set_ylabel('Reps')
    ax.set_zlabel('Mean deviation')
    plt.show()

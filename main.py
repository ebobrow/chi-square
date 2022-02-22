import pandas as pd
import matplotlib.pyplot as plt
from functools import partial
import time

q_95 = partial(pd.Series.quantile, q=0.95)
q_95.__name__ = "95%"

q_99 = partial(pd.Series.quantile, q=0.99)
q_99.__name__ = "99%"


def main(data):
    start = time.time()
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
        "10": [18.31, 23.21]
    },
        index=['95%', '99%'])

    table = df.agg([q_95, q_99])
    diff = table.subtract(expected).abs()

    elapsed = time.time() - start
    print("Python finished in %d seconds" % elapsed)

    # Show 95th and 99th quantile
    print(table)

    # Show difference from expected
    print("\nDifference: \n")
    print(diff)

    # Display graphs
    # df.plot.hist(subplots=True, bins=20)
    # plt.show()

    # Write to file
    with open("README.md", "w") as file:
        file.write("# Chi Square\n\n")
        file.write(table.to_markdown())
        file.write("\n## Difference from actual values\n\n")
        file.write(diff.to_markdown())


def mean_dif(data):
    expected = pd.DataFrame({
        1: [3.841, 6.635],
        2: [5.991, 9.210],
        3: [7.815, 11.34],
        4: [9.488, 13.28],
        5: [11.07, 15.09],
    },
        index=['95%', '99%'])

    df = pd.DataFrame(data)
    df = df[sorted(df.columns)]
    return df.agg([q_95, q_99]).subtract(expected).abs().mean().mean()


def accuracy(data):
    start = time.time()
    # TODO: This is slow
    results = pd.DataFrame(data).applymap(mean_dif).mean()

    elapsed = time.time() - start
    print("Python finished in %d seconds" % elapsed)

    sets, reps = zip(*results.index)
    ax = plt.figure().add_subplot(projection='3d')
    ax.scatter(sets, reps, results.values)
    ax.set_xlabel('Sets')
    ax.set_ylabel('Reps')
    ax.set_zlabel('Mean deviation')
    plt.show()

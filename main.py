import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import partial

q_95 = partial(pd.Series.quantile, q=0.95)
q_95.__name__ = "95%"

q_99 = partial(pd.Series.quantile, q=0.99)
q_99.__name__ = "99%"

def main(data):
    df = pd.DataFrame(data)
    df = df[sorted(df.columns)]
    expected = pd.DataFrame({
                                1:[3.841, 6.635],
                                2:[5.991, 9.210],
                                3:[7.815, 11.34],
                                4:[9.488, 13.28],
                                5:[11.07, 15.09]
                            },
                            index=['95%', '99%'])

    # Show 95th and 99th quantile
    table = df.agg([q_95, q_99])
    print(table)

    # Show difference from expected
    # print(table.subtract(expected))

    # Display graphs
    # df.plot.hist(subplots=True, bins=20)
    # plt.show()

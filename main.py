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
    print(df.agg([q_95, q_99]))
    df.plot.hist(subplots=True, bins=20)
    plt.show()

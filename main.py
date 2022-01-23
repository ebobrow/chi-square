import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main(data):
    df = pd.DataFrame(data)
    df = df[sorted(df.columns)]
    # print(df)
    for label, content in df.iteritems():
        print(str(label) + ": " + str(np.percentile(content, 95)))
    df.plot.hist(subplots=True, bins=20)
    plt.show()

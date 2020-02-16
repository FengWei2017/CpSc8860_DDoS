#!/usr/bin/env python
import matplotlib.pyplot as plt
from itertools import groupby

def plot_time_series(arrive_time):
    data=[int(item) for item in arrive_time]        # Round down
    y=[]                                            # List for plot
    i=0
    for key, group in groupby(data):                # Get time series
        if i!=key:                                  # Packets might not arrive at each second
            y+=[0]*(key-i)
        i=key+1
        y.append(len(list(group)))
    plt.plot(range((len(y))),y)                     # Plot
    plt.show()                                      # Show plot
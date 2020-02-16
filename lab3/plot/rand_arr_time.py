#!/usr/bin/env python
"""
Get random arrival time
"""

from scipy.stats import truncnorm
import numpy as np
import random

def rand_arr_time(option,number_of_packets,duratation):
    """
    options:
    0 Random
    1 Uniform
    2 Tnorm
    3 Poisson
    4 Exponential
    5 Poisson with random expectation of interval
    6 Randomly pick one of above functions
    """
    out=[]
    timestamp=0.0
    out.append(timestamp)
    rand_range=2*float(duratation)/float(number_of_packets)
    if option==0:
        for i in range(number_of_packets):
            timestamp+=random.random()*rand_range
            out.append(timestamp)
    elif option==1:
        for i in range(number_of_packets):
            timestamp+=random.uniform(0,rand_range)
            out.append(timestamp)
    elif option==2:
        for i in range(number_of_packets):
            timestamp+=truncnorm.rvs(0,rand_range)
            out.append(timestamp)
    elif option==3:
        for i in range(number_of_packets):
            timestamp+=np.random.poisson(rand_range/2)
            out.append(timestamp)
    elif option==4:
        for i in range(number_of_packets):
            timestamp+=np.random.exponential(rand_range/2)
            out.append(timestamp)
    elif option==5:
        for i in range(number_of_packets):
            timestamp+=np.random.poisson(random.random()*rand_range)
            out.append(timestamp)
    elif option==6:
        for i in range(number_of_packets):
            temp=rand_arr_time(random.randint(0, 5),1,0.01)
            timestamp += float(temp[1])
            out.append(timestamp)
    return out

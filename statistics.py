"""
Statistics module for MicroPython :
https://github.com/rcolistete/MicroPython_Statistics
Version: 0.4.1 @ 2018/10/19
Author: Roberto Colistete Jr. (roberto.colistete at gmail.com)
License: MIT License (https://opensource.org/licenses/MIT)
"""

import math

def mean(data):
    if iter(data) is data:
        data = list(data)
    return sum(data)/len(data)

def harmonic_mean(data):
    if iter(data) is data:
        data = list(data)
    return len(data)/sum([1/x for x in data])

def median(data):
    data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return data[n//2]
    else:
        i = n//2
        return (data[i - 1] + data[i])/2

def median_low(data):
    data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return data[n//2]
    else:
        return data[n//2 - 1]

def median_high(data):
    data = sorted(data)
    n = len(data)
    return data[n//2]

def median_grouped(data, interval=1):
    data = sorted(data)
    n = len(data)
    x = data[n//2]
    L = x - interval/2
    l1 = l2 = n//2
    while (l1 > 0) and (data[l1 - 1] == x):
        l1 -= 1
    while (l2 < n) and (data[l2 + 1] == x):
        l2 += 1
    return L + (interval*(n/2 - l1)/(l2 - l1 + 1))
        
def mode(data):
    if iter(data) is data:
        data = list(data)
    data = sorted(data)
    last = modev = None
    countmax = i = 0
    while i < len(data):
        if data[i] == last:
            count += 1
        else:
            count = 1
            last = data[i]
        if count > countmax:
            countmax = count
            modev = last
        i += 1
    return modev

def variance(data, xbar=None):
    if iter(data) is data:
        data = list(data)
    if xbar is None:
        xbar = sum(data)/len(data)
    total = sum([(x - xbar)**2 for x in data])
    total -= sum([(x - xbar) for x in data])**2/len(data)
    return total/(len(data) - 1)

def pvariance(data, mu=None):
    if iter(data) is data:
        data = list(data)
    if mu is None:
        mu = sum(data)/len(data)
    total = sum([(x - mu)**2 for x in data])
    total -= sum([(x - mu) for x in data])**2/len(data)
    return total/len(data)

def stdev(data, xbar=None):
    if iter(data) is data:
        data = list(data)
    if xbar is None:
        xbar = sum(data)/len(data)
    total = sum([(x - xbar)**2 for x in data])
    total -= sum([(x - xbar) for x in data])**2/len(data)
    return math.sqrt(total/(len(data) - 1))

def pstdev(data, mu=None):
    if iter(data) is data:
        data = list(data)
    if mu is None:
        mu = sum(data)/len(data)
    total = sum([(x -  mu)**2 for x in data])
    total -= sum([(x - mu) for x in data])**2/len(data)
    return math.sqrt(total/len(data))

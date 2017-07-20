import numpy as np

def mean(x):
    return sum(x)/len(x)
def std(x,sample = True):
    avg = mean(x)
    return np.sqrt(sum([(val -avg)**2 for val in x])/(len(x)-int(sample)))
def skew (x):
    return moment(x,3,True)/std(x)
def kurtosis(x):
    return (moment(x,4,True)/(moment(x,2,True)**2))
def moment(x,n, mu =False, sig = False):
    l = len(x)
    avg = mean(x)
    sigma = std(x,sample =False)
    if not sig:
        return sum([(val-int(mu)*avg)**n for val in x ])/l
    else:
        return sum([((val-int(mu)*avg)/sigma)**n for val in x])/l
#swagp

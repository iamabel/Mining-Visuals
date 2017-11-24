import numpy as np

def create2Clustering(N, D):
    cluster = np.empty([N,D])
    for i in range(N):
        for j in range(D):
            if i % 2 == 0:
                cluster[i,j] = 1 + .05*np.random.rand()
            else:
                cluster[i,j] = -1 - .05*np.random.rand()

    return cluster

def miyanoGrouping():
    grouping = np.random.normal(0, .1, (15,3))
    grouping[0:5, 0] += 1
    grouping[5:10, 1] += 1
    grouping[10:, 2] += 1

    return grouping

def flagData():
    # Work around funky 'b' addition from numpy loadtxt
    flags = np.loadtxt(fname="datasets/flag.data", dtype=bytes, delimiter=',').astype(str)
    locales = flags[:,0]

    print("Legend:")
    for i in range(len(locales)):
        print("\t"+str(i)+ ". "+locales[i])

    return np.delete(flags, (0,17,28,29), axis=1).astype(float)
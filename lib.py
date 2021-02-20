import networkx as nx
from networkx.convert_matrix import to_numpy_array
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.construct import random
seed = 123
np.random.seed(seed)

def random_network_ER_np(n,p,seed=seed):
    G=nx.gnp_random_graph(n,p,seed)
    A = nx.to_numpy_array(G)
    return A

def random_network_ER_nm(n,m,seed=seed):
    G=nx.gnm_random_graph(n,m,seed)
    A = nx.to_numpy_array(G)
    return A

def random_directed(n,p):
    A= np.zeros(shape=(n,n))
    for i in range(n):
        for j in range(n):
            if (np.random.rand()<p):
                A[i][j] = 1
    return A


def random_directed_noSelfLoops(n,p):
    A= np.zeros(shape=(n,n))
    for i in range(n):
        for j in range(n):
            if (j!=i and np.random.rand()<p):
                A[i][j] = 1
    return A

def random_directed_noLoops(n,p):
    A= np.zeros(shape=(n,n))
    for i in range(n):
        for j in range(n):
            if (j!=i and A[j][i]!=1 and np.random.rand()<p):
                A[i][j] = 1
    return A

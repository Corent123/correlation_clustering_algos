import numpy as np
import pulp
#import matplotlib.pyplot as plt
#import networkx as nx
from random import shuffle, random, randint
import modele

def optimal_clustering_cost(size: int, M:np.ndarray) -> int:

    if M.ndim != 2 or M.shape[0] != size or M.shape[1] != size:
        raise Exception("M has wrong shape")
    
    lp_problem = modele.convert_to_lp_problem(size, M)
    if(lp_problem.variables() == []): #graph has no bad triangles, so lp_problem has no variables
        return 0
    lp_problem.solve(pulp.PULP_CBC_CMD(msg=False))
    return pulp.value(lp_problem.objective)


def pivot(size: int, M: np.ndarray) -> np.ndarray:

    if M.ndim != 2 or M.shape[0] != size or M.shape[1] != size:
        raise Exception("M has wrong shape")

    clusters = np.zeros((size), dtype= np.int16)
    remainingVertices = [i for i in range(size)]
    shuffle(remainingVertices)
    clusterNumber = 1
    while(len(remainingVertices) > 0):
        v = remainingVertices.pop()
        clusters[v] = clusterNumber
        i = 0
        while i < len(remainingVertices):
            w = remainingVertices[i]
            if(M[v][w] == 1):
                remainingVertices.pop(i)
                clusters[w] = clusterNumber
            else:
                i += 1
        clusterNumber += 1
    return clusters

def pivot_adjacency_list(size: int, A: np.ndarray) -> np.ndarray:

    clusters = np.zeros((size), dtype= np.int16)
    remainingVertices = [i for i in range(size)]
    shuffle(remainingVertices)
    clusterNumber = 1
    while(len(remainingVertices) > 0):
        piv = remainingVertices.pop()
        clusters[piv] = clusterNumber
        for neighboor in A[piv]:
            if(clusters[neighboor] == 0):
                clusters[neighboor] = clusterNumber
        clusterNumber += 1
    return clusters


def ordered_pivot(size: int, M: np.ndarray) -> np.ndarray:
    """
    calculate the clusters

    Args:
        size (int) : the number of vertices
        M (ndarray[int][int]) : the 'adjacency' matrix of the clique
        permutation (list[int]) : the order of the vertices
    
    Returns
        ndarray[int] : associates to each vertex a cluster between 1 and the total number of clusters 

    """
    if M.ndim != 2 or M.shape[0] != size or M.shape[1] != size:
        raise Exception("M has wrong shape")

    clusters = np.zeros((size), dtype = np.int16)
    remainingVertices = [i for i in range(size)]
    shuffle(remainingVertices)
    currentCluster = []
    clusterNumber = 1
    while(len(remainingVertices) > 0):
        i = 0
        while i<len(remainingVertices):
            v = remainingVertices[i]
            acc = 0
            for w in currentCluster:
                acc += M[v][w]
            if(acc >= 0):
                remainingVertices.pop(i)
                currentCluster.append(v)
                clusters[v] = clusterNumber
            else:
                i += 1
        currentCluster.clear()
        clusterNumber += 1
    return clusters


def semi_ordered_pivot(size: int, M: np.ndarray) -> np.ndarray:
    """
    calculate the clusters

    Args:
        size (int) : the number of vertices
        M (ndarray[int][int]) : the 'adjacency' matrix of the clique
        permutation (list[int]) : the order of the vertices
    
    Returns
        ndarray[int] : associates to each vertex a cluster between 1 and the total number of clusters 

    """
    if M.ndim != 2 or M.shape[0] != size or M.shape[1] != size:
        raise Exception("M has wrong shape")

    clusters = np.zeros((size), dtype= np.int16)
    remainingVertices = [i for i in range(size)]
    shuffle(remainingVertices)
    currentCluster = []
    clusterNumber = 1
    while(len(remainingVertices) > 0):
        i = 0
        while i<len(remainingVertices):
            v = remainingVertices[i]
            acc = 0
            for w in currentCluster:
                acc += M[v][w]
            if(acc >= 0):
                remainingVertices.pop(i)
                currentCluster.append(v)
                clusters[v] = clusterNumber
            else:
                i += 1
        currentCluster.clear()
        clusterNumber += 1
        shuffle(remainingVertices)
    return clusters


        

def concurrent_clusters(size: int, M: np.ndarray) -> np.ndarray:

    if M.ndim != 2 or M.shape[0] != size or M.shape[1] != size:
        raise Exception("M has wrong shape")

    clusters = np.zeros((size), dtype=np.int32)
    permutation = [i for i in range(size)]
    shuffle(permutation)
    clusterNumber = 1
    for i in range(size):
        v = permutation[i]
        clustersCost = [0 for i in range(clusterNumber)]
        for j in range(i):
            w = permutation[j]
            clustersCost[clusters[w]-1] += M[v][w]
        maxCost = (-1,-1)
        for c in range(clusterNumber):
            if(maxCost[1] < clustersCost[c]):
                maxCost = (c, clustersCost[c])
        if(maxCost[1] >= 0):
            clusters[v] = maxCost[0] + 1
        else:
            clusterNumber += 1
            clusters[v] = clusterNumber
    return clusters

def vote_adjacency_list(size: int, A: np.ndarray[list[int]]) -> np.ndarray[int]:

    clusters = np.zeros((size), dtype=np.int32)
    cluster_sizes = [0 for i in range((size)**(1/2))]
    permutation = [i for i in range(size)]
    shuffle(permutation)
    clusterNumber = 1
    for i in range(size):
        v = permutation[i]
        clustersCost = {}
        for w in A[v]:
            if(clusters[w] != 0):
                if(clustersCost.get(clusters[w] == None)):
                    clustersCost[clusters[w]] = - cluster_sizes[clusters[w]] # cost is 2*(+ edges) - (edges)

                clustersCost[clusters[w]] += 2
        maxCost = (0,-1)
        for cluster, cost in clustersCost.items():
            if(maxCost[1] < cost):
                maxCost = (cluster, cost)
        if(maxCost[1] >= 0):
            clusters[v] = maxCost[0]
            cluster_sizes[maxCost[0]] += 1
        else:
            clusterNumber += 1
            clusters[v] = clusterNumber
            if(len(cluster_sizes) < clusterNumber):
                cluster_sizes.append(1)
            else:
                cluster_sizes[clusterNumber-1] += 1
    return clusters


def local_search(size: int, A: np.ndarray[list[int]], clusters: np.ndarray[int], permutation: np.ndarray[int]) -> np.ndarray[int]:
    pass

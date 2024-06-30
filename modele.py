import numpy as np
import networkx as nx
import pulp
from random import shuffle, random, randint

def clustering_cost(size: int, M: np.ndarray, clusters: np.ndarray) -> int:
    cost = 0
    for i in range(size):
        for j in range(i+1, size):
            if(M[i][j] == 1 and clusters[i] != clusters[j]):
                cost += 1
            elif(M[i][j] == -1 and clusters[i] == clusters[j]):
                cost += 1
    return cost


def random_valuation_matrix(size: int, p: float) -> np.ndarray:
    """
    

    Args:
        size (int) : the size of the matrix
        p (float) : probability of a + edge, between 0 and 1

    Return:
        (np.ndarray[int][int]) : the adjacency matrix
    
    """
    M = np.zeros((size,size), dtype=np.int8)
    for i in range(size):
        for j in range(i+1,size):
            if(random() < p):
                M[i][j] = 1
                M[j][i] = 1
            else:
                M[i][j] = -1
                M[j][i] = -1
    return M



def perfectly_clustered_with_flipped_edges(size: int, k: int, f: int) -> np.ndarray:
    """
    a graph perfectly clustered in k clusters where f edges have been flipped

    Args:
        size (int) : the number of vertices
        k (int) : the number of clusters
        f (int) : the number of edges to flip
    
    Returns
        ndarray[int][int] : the adjacency matrix of the graph

    """
    M = np.zeros((size,size), dtype=np.int8)
    clusters = np.zeros((size), dtype=np.int16)
    for i in range(size):
        clusters[i] = randint(1,k)
    
    for i in range(size):
        for j in range(i+1, size):
            if(clusters[i] == clusters[j]):
                M[i][j] = 1
                M[j][i] = 1
            else:
                M[i][j] = -1
                M[j][i] = -1
    vertices = [(i,j) for i in range(size) for j in range(i+1, size)]
    shuffle(vertices)
    for a in range(f):
        (i,j) = vertices[a]
        M[i][j] = - M[i][j]
        M[j][i] = - M[j][i]
    return M





def convert_to_lp_problem(size: int, M: np.ndarray) -> pulp.LpProblem:

    if M.ndim != 2 or M.shape[0] != size or M.shape[1] != size:
        raise Exception("M has wrong shape")

    lp_problem = pulp.LpProblem("clustering", pulp.LpMinimize)
    badEdges = {}
    badEdgesBis = {}
    varSum = pulp.LpAffineExpression()

    for i in range(size):
        for j in range(i+1, size):
            for k in range(j+1, size):
                sumOfEdges = M[i][j] + M[j][k] + M[i][k]
                if(sumOfEdges == 1):  #bad triangle
                    name = str(i)+"_"+str(j)+"_"+str(k)
                    for l in [(i,j),(i,k),(j,k)]:
                        if (type(badEdges.get(l)) == type(None)):
                            var = pulp.LpVariable("x"+str(l[0])+"_"+str(l[1]), lowBound=0, upBound=1, cat=pulp.LpInteger)
                            badEdges[l] = var
                            badEdgesBis[l] = True
                            varSum += var
                    lp_problem += badEdges[(i,j)] + badEdges[(i,k)] + badEdges[(j,k)] >= 1
    lp_problem.setObjective(varSum)
    return lp_problem


def graph_to_valuation_matrix(graph: nx.Graph) -> np.ndarray:
    """
    transforms a networkx undirected simple graph to a valuation matrix where a non-edges are represented by -1
    """
    size = graph.number_of_nodes()
    M = nx.to_numpy_array(graph, dtype=np.int8)
    for i in range(0, size):
        for j in range(i+1, size):
            if(M[i][j] == 0):
                M[i][j] = -1
                M[j][i] = -1
    return M

def graphs_to_valuation_matrices(graphs: list[nx.Graph]) -> np.ndarray[np.ndarray]:
    array = np.empty(len(graphs), dtype = np.ndarray)
    for i in range(len(graphs)):
        g = graphs[i]
        array[i] = graph_to_valuation_matrix(g)
    return array

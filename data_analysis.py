import numpy as np
import pulp
import networkx as nx
from random import shuffle, random, randint
import modele, algo, methodology, manage_files


def sum_stats(file_name: str) -> np.ndarray:
    stats = manage_files.load_object(file_name)
    return np.sum(stats, axis=0)


def compare_stats(file_name_1, file_name_2) -> np.ndarray[(int, int), np.float128]:
    """
    compare stats about two approximation algorithms on the same set of graphs. 

    Returns:

        (np.ndarray[(n, 10), np.float128]) : for each value : 
            - number of times where the first is lower than the second
            - number of times where the first is equal to the second
            - number of times where the first is greater than the second
            - the average of the first
            - the average of the second
            - the average difference between the first and the second, in percentages
            - the biggest difference between the two where the first is lower
            - the biggest difference between the two where the first is greater
            - the sum of the first
            - the sum of the second
    """

    stats1 = manage_files.load_object(file_name_1)
    stats2 = manage_files.load_object(file_name_2)

    if(stats1.shape != stats2.shape):
        raise Exception("Shapes are incompatible")

    res = np.zeros((stats1.shape[1], 12), dtype= float)


    for j in range(stats1.shape[1]):
        res[j][3] = np.sum(stats1, axis=0)[j]/stats1.shape[0]
        res[j][4] = np.sum(stats2, axis=0)[j]/stats2.shape[0]
        if(res[j][4] == 0):
            res[j][5] = 0 if res[j][3] == 0 else np.inf
        else:
            res[j][5] = (res[j][3] - res[j][4])*100/(res[j][4])
        a = 100*np.divide((stats1 - stats2),stats2, out = np.zeros_like(stats1), where = stats2!=0)
        res[j][6] = np.mean(a, axis=0)[j]
        res[j][7] = np.std(a, axis=0)[j]

        res[j][8] = np.sum(stats1, axis=0)[j]
        res[j][9] = np.sum(stats2, axis=0)[j]

        for i in range(stats1.shape[0]):
            if(stats1[i][j] < stats2[i][j]):
                res[j][0] += 1
            if(stats1[i][j] == stats2[i][j]):
                res[j][1] += 1
            if(stats1[i][j] > stats2[i][j]):
                res[j][2] += 1
            if(stats1[i][j] - stats2[i][j] < res[j][6]):
                res[j][10] = stats1[i][j] - stats2[i][j]
            if(stats1[i][j] - stats2[i][j] > res[j][7]):
                res[j][11] = stats1[i][j] - stats2[i][j]
        
    
    return res


def get_important_stats(file_name_1, file_name_2) -> np.ndarray:
    """
    returns the difference in percentage in average cost and average number of clusters between the two files and stnadard deviation for both
    """
    cs = compare_stats(file_name_1, file_name_2)
    return np.array([cs[2][6],cs[2][7],cs[6][6],cs[6][7]], dtype=float)


def avg_cost_clusters_multiple_files(file_names1: list, file_names2: list) -> np.ndarray:
    res = np.empty((2), dtype=float)
    costs = [get_important_stats(file_names1[i], file_names2[i])[0] for i in range(len(file_names1))]
    nb_clusters = [get_important_stats(file_names1[i], file_names2[i])[2] for i in range(len(file_names1))]
    sizes = [manage_files.load_object(file_names1[i]).shape[0] for i in range(len(file_names1))]
    total_size = sum(sizes)
    for i in range(len(file_names1)):
        res[0] += ((costs[i])*(sizes[i]))/total_size
        res[1] += ((nb_clusters[i])*(sizes[i]))/total_size
    return res

def get_max_stats(filename):
    s = manage_files.load_object(filename)
    return np.max(s, axis = 0)

def get_average_stats(filename):
    s = manage_files.load_object(filename)
    return np.mean(s, axis = 0)
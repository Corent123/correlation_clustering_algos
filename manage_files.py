import networkx as nx
import numpy as np
import pickle
import modele
import csv
from collections import defaultdict

def read_graph6(filename: str) -> list[nx.Graph]:
    l = nx.read_graph6(filename)

    if type(l) == nx.Graph:
        return [l]
    if type(l) == list:
        return l
    raise Exception("l has wrong type")


def graph6_to_valuation_matrices(filename: str) -> np.ndarray[np.ndarray]:
    graphs = read_graph6(filename)
    return modele.graphs_to_valuation_matrices(graphs)

def store_graph_6_as_valuation_matrices(g6_file: str, store_file: str) -> None:
    matrices = graph6_to_valuation_matrices(g6_file)
    store_object(store_file, matrices)
    

def store_object(filename: str, obj) -> None:

    with open(filename, 'wb') as f:
        pickle.dump(obj, f)
    

def load_object(filename):
    
    with open(filename, 'rb') as f:
        obj = pickle.load(f)
    
    return obj


def read_large_network_relabel(file_name, delimiter):
    """Read in 0/1 graph from social network, input as adjacency list
    Relabel nodes as we encounter them, in case of non-contiguous numbering in data file
    """

    my_mapping = defaultdict(int)
    my_graph = defaultdict(list)

    try:
        with open(file_name, 'r') as my_reader:
            reader = csv.reader(my_reader, delimiter=delimiter)

            # Get the number of points from the first line
            num_pts = int(next(reader)[0])

            cur_index = 0
            for row in reader:
                x, y = int(row[0]), int(row[1])

                # RELABEL
                if x not in my_mapping:
                    my_mapping[x] = cur_index
                    cur_index += 1

                if y not in my_mapping:
                    my_mapping[y] = cur_index
                    cur_index += 1

                # ADD TO GRAPH
                map_x, map_y = my_mapping[x], my_mapping[y]
                if map_x != map_y:  # avoid self-edges
                    my_graph[map_x].append(map_y)
                    my_graph[map_y].append(map_x)

        return np.array(my_graph, dtype=int)
    except Exception as e:
        print("")
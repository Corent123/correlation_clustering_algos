import numpy as np
import pulp
import modele, algo, manage_files


def test_graph(size: int, M: np.ndarray, approx_algo, nb_of_tries: int = 10) -> tuple[int, int, int, int]:
    costs = np.zeros((nb_of_tries), dtype=np.int32)
    nb_of_clusters = np.zeros((nb_of_tries), dtype=np.int32)
    for i in range(nb_of_tries):
        clusters = approx_algo(size, M)
        nb_of_clusters[i] = clusters.max()
        cost = modele.clustering_cost(size, M, clusters)
        costs[i] = cost
    return (costs.min(), costs.max(), costs.mean(), costs.std(), nb_of_clusters.min(), nb_of_clusters.max(), nb_of_clusters.mean(), nb_of_clusters.std())



def store_graphs_test(graphs: np.ndarray[np.ndarray], filename: str, approx_algo) -> None:
    """
    applies funtion to each graph in graphs and store the results as a list in file named filename

    Args:
        graphs (np.ndarray[np.ndarray]) : an array of the valuation matrices of the graphs
    
    """

    result = np.array([function(g) for g in graphs])
    manage_files.store_object(result)


def apply_algo_to_folder(folder_name: str, size: int, approx_algo, algo_name: str, nb_of_tries: int = 10, save_clusters: bool = True, save_stats: bool = True) -> None:
    """
    try the approximation algorithm on all graphs in graphs/folder_name/folder_name_graphs.pickle
    
    Args:
        folder_name (str) : the name of the folder where the "foldername_graphs" file is
        algo_name (str) : the name to add at the end of foldername
        size (int) : the number of nodes of graphs in the foldername_graphs file
        approx_algo : the approximation algorithm to use
        nb_of_tries (int) : the number of calls of approx_algo on each graph
        save_clusters (bool) : if True, saves the clusters in file foldername_name_"clusters"
        save_stats (bool) : if True, saves stats in file foldername_name_"stats"

    """
    if (not save_clusters) and (not save_stats):
        return

    file_name = "graphs/" + folder_name + "/" + folder_name
    graphs_file_name = file_name + "_graphs.pickle"
    graphs = manage_files.load_object(graphs_file_name)
    clusters = np.empty((len(graphs), nb_of_tries), dtype=np.ndarray)
    stats = np.empty((len(graphs), 8), dtype=np.float128)
    nb_of_graphs = len(graphs)
    print_percentages = [i for i in range(1,102)]

    for i in range(nb_of_graphs):
        if ((int(i*100/nb_of_graphs) > print_percentages[0])):
            print(str(print_percentages[0]) + "% done")
            print_percentages.pop(0)
        g = graphs[i]
        for j in range(nb_of_tries):
            clusters[i][j] = approx_algo(size, g)

        if(save_stats):
            costs = np.empty((nb_of_tries), dtype=np.int32)
            nb_of_clusters = np.empty((nb_of_tries), dtype=np.int32)
            for j in range(nb_of_tries):

                nb_of_clusters[j] = (clusters[i][j]).max()
                cost = modele.clustering_cost(size, g, clusters[i][j])
                costs[j] = cost
            stats[i] = np.array([costs.min(), costs.max(), costs.mean(), costs.std(), nb_of_clusters.min(), nb_of_clusters.max(), nb_of_clusters.mean(), nb_of_clusters.std()], dtype=np.float128)

    if(save_clusters):
        manage_files.store_object(file_name + "_" + algo_name + "_clusters.pickle", clusters)

    if(save_stats):
        manage_files.store_object(file_name + "_" + algo_name + "_stats.pickle", stats)
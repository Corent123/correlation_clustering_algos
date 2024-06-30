import numpy as np
import pulp
import networkx as nx
from random import shuffle, random, randint
import modele, algo, methodology, manage_files, data_analysis
import multiprocessing





# stores the g6 files as lists of valuation matrices

# manage_files.store_graph_6_as_valuation_matrices("graphs/all3n/graph3.g6", "graphs/all3n/all3n_graphs.pickle")
# manage_files.store_graph_6_as_valuation_matrices("graphs/all4n/graph4.g6", "graphs/all4n/all4n_graphs.pickle")
# manage_files.store_graph_6_as_valuation_matrices("graphs/all5n/graph5.g6", "graphs/all5n/all5n_graphs.pickle")
# manage_files.store_graph_6_as_valuation_matrices("graphs/all6n/graph6.g6", "graphs/all6n/all6n_graphs.pickle")
# manage_files.store_graph_6_as_valuation_matrices("graphs/all7n/graph7.g6", "graphs/all7n/all7n_graphs.pickle")
# manage_files.store_graph_6_as_valuation_matrices("graphs/all8n/graph8.g6", "graphs/all8n/all8n_graphs.pickle")
# manage_files.store_graph_6_as_valuation_matrices("graphs/all9n/graph9.g6", "graphs/all9n/all9n_graphs.pickle")



# stores the clusters and stats

# # all 3 nodes graphs
# methodology.apply_algo_to_folder("all3n", 3, algo.pivot, "pivot", 5)
# methodology.apply_algo_to_folder("all3n", 3, algo.ordered_pivot, "ord_pivot", 5)
# methodology.apply_algo_to_folder("all3n", 3, algo.semi_ordered_pivot, "semi_ord_pivot", 5)
# methodology.apply_algo_to_folder("all3n", 3, algo.concurrent_clusters, "concurrent", 5)

# # all 4 nodes graphs
# methodology.apply_algo_to_folder("all4n", 4, algo.pivot, "pivot", 10)
# methodology.apply_algo_to_folder("all4n", 4, algo.ordered_pivot, "ord_pivot", 10)
# methodology.apply_algo_to_folder("all4n", 4, algo.semi_ordered_pivot, "semi_ord_pivot", 10)
# methodology.apply_algo_to_folder("all4n", 4, algo.concurrent_clusters, "concurrent", 10)

# # all 5 nodes graphs
# methodology.apply_algo_to_folder("all5n", 5, algo.pivot, "pivot", 10)
# methodology.apply_algo_to_folder("all5n", 5, algo.ordered_pivot, "ord_pivot", 10)
# methodology.apply_algo_to_folder("all5n", 5, algo.semi_ordered_pivot, "semi_ord_pivot", 10)
# methodology.apply_algo_to_folder("all5n", 5, algo.concurrent_clusters, "concurrent", 10)

# # all 6 nodes graphs
# methodology.apply_algo_to_folder("all6n", 6, algo.pivot, "pivot", 10)
# methodology.apply_algo_to_folder("all6n", 6, algo.ordered_pivot, "ord_pivot", 10)
# methodology.apply_algo_to_folder("all6n", 6, algo.semi_ordered_pivot, "semi_ord_pivot", 10)
# methodology.apply_algo_to_folder("all6n", 6, algo.concurrent_clusters, "concurrent", 10)

# # all 7 nodes graphs
# methodology.apply_algo_to_folder("all7n", 7, algo.pivot, "pivot", 10)
# methodology.apply_algo_to_folder("all7n", 7, algo.ordered_pivot, "ord_pivot", 10)
# methodology.apply_algo_to_folder("all7n", 7, algo.semi_ordered_pivot, "semi_ord_pivot", 10)
# methodology.apply_algo_to_folder("all7n", 7, algo.concurrent_clusters, "concurrent", 10)

# # all 8 nodes graphs
# methodology.apply_algo_to_folder("all8n", 8, algo.pivot, "pivot", 10)
# methodology.apply_algo_to_folder("all8n", 8, algo.ordered_pivot, "ord_pivot", 10)
# methodology.apply_algo_to_folder("all8n", 8, algo.semi_ordered_pivot, "semi_ord_pivot", 10)
# methodology.apply_algo_to_folder("all8n", 8, algo.concurrent_clusters, "concurrent", 10)

# all 9 nodes graphs
# methodology.apply_algo_to_folder("all9n", 9, algo.pivot, "pivot", 10)
# methodology.apply_algo_to_folder("all9n", 9, algo.ordered_pivot, "ord_pivot", 10)
# methodology.apply_algo_to_folder("all9n", 9, algo.semi_ordered_pivot, "semi_ord_pivot", 10)
# methodology.apply_algo_to_folder("all9n", 9, algo.concurrent_clusters, "concurrent", 10)

# for n in range(3,10):
#     print(n)
#     name = "graphs/all"+str(n)+"n/all"+str(n)+"n_graphs.pickle"
#     graphs = manage_files.load_object(name)
#     res = np.empty(graphs.shape[0], dtype= int)
#     print_percentages = [10*i for i in range(1,12)]
#     nb_of_graphs = graphs.shape[0]
#     for i in range(graphs.shape[0]):
#         if (len(print_percentages)> 0 and ((int(i*100/nb_of_graphs) > print_percentages[0]))):
#             print(str(print_percentages[0]) + "% done")
#             print_percentages.pop(0)
#         graph = graphs[i]
#         cost = algo.optimal_clustering_cost(n, graph)
#         res[i] = cost
#     manage_files.store_object("graphs/all"+str(n)+"n/all"+str(n)+"n_opt_cost.pickle", res)
    



# random graphs of 100 nodes

# generation

# folder_name = "1000rnd100n"

# for t in [(0.05,"005"),(0.1,"01"),(0.2,"02"),(0.3,"03"),(0.4,"04"),(0.5,"05"),(0.6,"06"),(0.7,"07"),(0.8,"08"),(0.9,"09"),(0.95,"095")]:
#     p = t[0]
#     strp = t[1]
#     l = np.array([modele.random_valuation_matrix(100, p) for i in range(1000)])
#     manage_files.store_object("graphs/" + folder_name + strp + "p/" + folder_name + strp +"p_graphs.pickle", l)

# for p in ["005","01","02","03","04","05","06","07","08","09","095"]:
#     name = "1000rnd100n" + p + "p"
#     methodology.apply_algo_to_folder(name, 100, algo.pivot, "pivot", 20)
#     methodology.apply_algo_to_folder(name, 100, algo.ordered_pivot, "ord_pivot", 20)
#     methodology.apply_algo_to_folder(name, 100, algo.semi_ordered_pivot, "semi_ord_pivot", 20)
#     methodology.apply_algo_to_folder(name, 100, algo.concurrent_clusters, "concurrent", 20)


# folder_name = "1000rnd100n"
# p = 0.55

# strp = "055"

# l = np.array([modele.random_valuation_matrix(100, p) for i in range(1000)])
# manage_files.store_object("graphs/" + folder_name + strp + "p/" + folder_name + strp +"p_graphs.pickle", l)

# name = "1000rnd100n" + "055" + "p"

# def task1():
#     methodology.apply_algo_to_folder("1000rnd100n" + "055" + "p", 100, algo.pivot, "pivot", 20)

# def task2():
#     methodology.apply_algo_to_folder("1000rnd100n" + "055" + "p", 100, algo.ordered_pivot, "ord_pivot", 20)

# def task3():    
#     methodology.apply_algo_to_folder("1000rnd100n" + "055" + "p", 100, algo.semi_ordered_pivot, "semi_ord_pivot", 20)
    
# def task4():    
#     methodology.apply_algo_to_folder("1000rnd100n" + "055" + "p", 100, algo.concurrent_clusters, "concurrent", 20)

# if __name__ == '__main__':
#     processes = [multiprocessing.Process(target=task1),
#                 multiprocessing.Process(target=task2),
#                 multiprocessing.Process(target=task3),
#                 multiprocessing.Process(target=task4)]

#     for process in processes:
#         process.start()

#     for process in processes:
#         process.join()




# folder_name = "100rnd200n"

# for t in [(0.05,"005"),(0.1,"01"),(0.2,"02"),(0.3,"03"),(0.4,"04"),(0.5,"05"),(0.6,"06"),(0.7,"07"),(0.8,"08"),(0.9,"09"),(0.95,"095")]:
#     p = t[0]
#     strp = t[1]
#     l = np.array([modele.random_valuation_matrix(200, p) for i in range(100)])
#     manage_files.store_object("graphs/" + folder_name + strp + "p/" + folder_name + strp +"p_graphs.pickle", l)

# for p in ["005","01","02","03","04","05","06","07","08","09","095"]:
#     print(p)
#     name = "100rnd200n" + p + "p"
#     methodology.apply_algo_to_folder(name, 200, algo.pivot, "pivot", 20)
#     methodology.apply_algo_to_folder(name, 200, algo.ordered_pivot, "ord_pivot", 20)
#     methodology.apply_algo_to_folder(name, 200, algo.semi_ordered_pivot, "semi_ord_pivot", 20)
#     methodology.apply_algo_to_folder(name, 200, algo.concurrent_clusters, "concurrent", 20)




# perfectly clustered graphs

# folder_name = "1000pfc100n5k"

# for t in [(25,"25"),(50,"50"),(100,"100"),(200,"200"),(400,"400"),(750,"750"),(1500,"1500"),(3000,"3000")]:
#     f = t[0]
#     strf = t[1]
#     l = np.array([modele.perfectly_clustered_with_flipped_edges(100, 5, f) for i in range(1000)])
#     manage_files.store_object("graphs/" + folder_name + strf + "f/" + folder_name + strf +"f_graphs.pickle", l)


# for f in ["25","50","100","200","400","750","1500","3000"]:
#     name = "1000pfc100n5k" + f + "f"
#     methodology.apply_algo_to_folder(name, 100, algo.pivot, "pivot", 20)
#     methodology.apply_algo_to_folder(name, 100, algo.ordered_pivot, "ord_pivot", 20)
#     methodology.apply_algo_to_folder(name, 100, algo.semi_ordered_pivot, "semi_ord_pivot", 20)
#     methodology.apply_algo_to_folder(name, 100, algo.concurrent_clusters, "concurrent", 20)



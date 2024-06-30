import numpy as np
import pulp
import networkx as nx
from random import shuffle, random, randint
import modele, algo, methodology, manage_files, data_analysis
import multiprocessing


np.set_printoptions(precision=3, suppress=True)

# a = np.array([
#     [0,1,2],
#     [-1,0,1]
# ])

# b = np.empty(4, dtype = np.int32)
# b[0] = 1
# print(b)

# a = np.array([0,1,2])

# print(type(a))



# cs = data_analysis.compare_stats("graphs/all7n/all7n_concurrent_stats.pickle","graphs/all7n/all7n_concurrent_stats.pickle")

# print(cs)

# print(data_analysis.sum_stats("graphs/all7n/all7n_concurrent_stats.pickle"))


# s = manage_files.load_object("graphs/all4n/all4n_concurrent_stats.pickle")

# print(s)

# print(s[0:2][0])

# lp = ["005","01","02","03","04","05","055","06","07","08","09","095"]

# conc = np.empty((12,4), dtype = np.float128)
# ord_pi = np.empty((12,4), dtype = np.float128)
# semi_ord_pi = np.empty((12,4), dtype = np.float128)

# conc_vs_ord = np.empty((12,4), dtype = np.float128)
# conc_vs_semi = np.empty((12,4), dtype = np.float128)
# ord_vs_semi = np.empty((12,4), dtype = np.float128)

# for i in range(12):
#     p = lp[i]
#     name_pivot = "graphs/" + "1000rnd100n" + p + "p/" + "1000rnd100n" + p + "p_" + "pivot" + "_stats.pickle"
#     name_ord_pi = "graphs/" + "1000rnd100n" + p + "p/" + "1000rnd100n" + p + "p_" + "ord_pivot" + "_stats.pickle"
#     name_semi_ord_pi = "graphs/" + "1000rnd100n" + p + "p/" + "1000rnd100n" + p + "p_" + "semi_ord_pivot" + "_stats.pickle"
#     name_conc = "graphs/" + "1000rnd100n" + p + "p/" + "1000rnd100n" + p + "p_" + "concurrent" + "_stats.pickle"

#     conc[i] = data_analysis.get_important_stats(name_conc, name_pivot)
#     ord_pi[i] = data_analysis.get_important_stats(name_ord_pi, name_pivot)
#     semi_ord_pi[i] = data_analysis.get_important_stats(name_semi_ord_pi, name_pivot)

#     conc_vs_ord[i] = data_analysis.get_important_stats(name_conc, name_ord_pi)
#     conc_vs_semi[i] = data_analysis.get_important_stats(name_conc, name_semi_ord_pi)

#     ord_vs_semi[i] = data_analysis.get_important_stats(name_ord_pi, name_semi_ord_pi)


# print(ord_pi)
# print()
# print(semi_ord_pi)
# print()
# print(conc)
# print()
# print(ord_vs_semi)
# print()
# print(conc_vs_ord)
# print()
# print(conc_vs_semi)


# p = "055"

# name_pivot = "graphs/" + "1000rnd100n" + p + "p/" + "1000rnd100n" + p + "p_" + "pivot" + "_stats.pickle"
# name_ord_pi = "graphs/" + "1000rnd100n" + p + "p/" + "1000rnd100n" + p + "p_" + "ord_pivot" + "_stats.pickle"
# name_semi_ord_pi = "graphs/" + "1000rnd100n" + p + "p/" + "1000rnd100n" + p + "p_" + "semi_ord_pivot" + "_stats.pickle"
# name_conc = "graphs/" + "1000rnd100n" + p + "p/" + "1000rnd100n" + p + "p_" + "concurrent" + "_stats.pickle"

# print(data_analysis.compare_stats(name_conc, name_pivot))


# a = np.array([
#     [1,1,2],
#     [4,5,6]
# ])

# b = np.array([
#     [2,3,5],
#     [8,9,10]
# ])

# print(np.std(100*(a-b)/b, axis = 0))





# lp = ["005","01","02","03","04","05","06","07","08","09","095"]

# conc = np.empty((len(lp),4), dtype = np.float128)
# ord_pi = np.empty((len(lp),4), dtype = np.float128)
# semi_ord_pi = np.empty((len(lp),4), dtype = np.float128)

# conc_vs_ord = np.empty((len(lp),4), dtype = np.float128)
# conc_vs_semi = np.empty((len(lp),4), dtype = np.float128)
# ord_vs_semi = np.empty((len(lp),4), dtype = np.float128)

# for i in range(len(lp)):
#     p = lp[i]
#     name_pivot = "graphs/" + "100rnd200n" + p + "p/" + "100rnd200n" + p + "p_" + "pivot" + "_stats.pickle"
#     name_ord_pi = "graphs/" + "100rnd200n" + p + "p/" + "100rnd200n" + p + "p_" + "ord_pivot" + "_stats.pickle"
#     name_semi_ord_pi = "graphs/" + "100rnd200n" + p + "p/" + "100rnd200n" + p + "p_" + "semi_ord_pivot" + "_stats.pickle"
#     name_conc = "graphs/" + "100rnd200n" + p + "p/" + "100rnd200n" + p + "p_" + "concurrent" + "_stats.pickle"

#     conc[i] = data_analysis.get_important_stats(name_conc, name_pivot)
#     ord_pi[i] = data_analysis.get_important_stats(name_ord_pi, name_pivot)
#     semi_ord_pi[i] = data_analysis.get_important_stats(name_semi_ord_pi, name_pivot)

#     conc_vs_ord[i] = data_analysis.get_important_stats(name_conc, name_ord_pi)
#     conc_vs_semi[i] = data_analysis.get_important_stats(name_conc, name_semi_ord_pi)

#     ord_vs_semi[i] = data_analysis.get_important_stats(name_ord_pi, name_semi_ord_pi)


# print(ord_pi)
# print()
# print(semi_ord_pi)
# print()
# print(conc)
# print()
# print(ord_vs_semi)
# print()
# print(conc_vs_ord)
# print()
# print(conc_vs_semi)



# lp = ["005","01","02","03","04","05","06","07","08","09","095"]

# conc = np.empty((len(lp),4), dtype = np.float128)
# ord_pi = np.empty((len(lp),4), dtype = np.float128)
# semi_ord_pi = np.empty((len(lp),4), dtype = np.float128)

# conc_vs_ord = np.empty((len(lp),4), dtype = np.float128)
# conc_vs_semi = np.empty((len(lp),4), dtype = np.float128)
# ord_vs_semi = np.empty((len(lp),4), dtype = np.float128)

# for i in range(len(lp)):
#     p = lp[i]
#     name_pivot = "graphs/" + "100rnd200n" + p + "p/" + "100rnd200n" + p + "p_" + "pivot" + "_stats.pickle"
#     name_ord_pi = "graphs/" + "100rnd200n" + p + "p/" + "100rnd200n" + p + "p_" + "ord_pivot" + "_stats.pickle"
#     name_semi_ord_pi = "graphs/" + "100rnd200n" + p + "p/" + "100rnd200n" + p + "p_" + "semi_ord_pivot" + "_stats.pickle"
#     name_conc = "graphs/" + "100rnd200n" + p + "p/" + "100rnd200n" + p + "p_" + "concurrent" + "_stats.pickle"

#     conc[i] = data_analysis.get_important_stats(name_conc, name_pivot)
#     ord_pi[i] = data_analysis.get_important_stats(name_ord_pi, name_pivot)
#     semi_ord_pi[i] = data_analysis.get_important_stats(name_semi_ord_pi, name_pivot)

#     conc_vs_ord[i] = data_analysis.get_important_stats(name_conc, name_ord_pi)
#     conc_vs_semi[i] = data_analysis.get_important_stats(name_conc, name_semi_ord_pi)

#     ord_vs_semi[i] = data_analysis.get_important_stats(name_ord_pi, name_semi_ord_pi)


# print(ord_pi)
# print()
# print(semi_ord_pi)
# print()
# print(conc)
# print()
# print(ord_vs_semi)
# print()
# print(conc_vs_ord)
# print()
# print(conc_vs_semi)



# name = "graphs/all"

# pivot = []
# ordered = []
# semi_ordered = []
# conc = []


# for n in [3,4,5,6,7,8,9]:
#     pivot.append(name+str(n)+"n/all"+str(n)+"n_pivot_stats.pickle")
#     ordered.append(name+str(n)+"n/all"+str(n)+"n_ord_pivot_stats.pickle")
#     semi_ordered.append(name+str(n)+"n/all"+str(n)+"n_semi_ord_pivot_stats.pickle")
#     conc.append(name+str(n)+"n/all"+str(n)+"n_concurrent_stats.pickle")

# def task1():
#     ord_vs_pi = data_analysis.avg_cost_clusters_multiple_files(ordered, pivot)
#     print("ord vs pi : \n",ord_vs_pi)

# def task2():
#     conc_vs_pi = data_analysis.avg_cost_clusters_multiple_files(conc, pivot)
#     print("conc vs pi : \n",conc_vs_pi)

# def task3():
#     conc_vs_ord = data_analysis.avg_cost_clusters_multiple_files(conc, ordered)
#     print("conc vs ord : \n",conc_vs_ord)

# def task4():
#     ord_vs_semi = data_analysis.avg_cost_clusters_multiple_files(ordered, semi_ordered)
#     print("ord vs semi : \n",ord_vs_semi)



# lf = ["25","50","100","200","400","750","1500","3000"]

# pivot = np.empty((8,8), dtype=np.float128)
# conc = np.empty((8,8), dtype = np.float128)
# ord_pi = np.empty((8,8), dtype = np.float128)
# semi_ord_pi = np.empty((8,8), dtype = np.float128)

# conc_vs_ord = np.empty((8,4), dtype = np.float128)
# conc_vs_semi = np.empty((8,4), dtype = np.float128)
# ord_vs_semi = np.empty((8,4), dtype = np.float128)

# for i in range(len(lf)):
#     f = lf[i]
#     name_pivot = "graphs/" + "1000pfc100n5k" + f + "f/" + "1000pfc100n5k" + f + "f_" + "pivot" + "_stats.pickle"
#     name_ord_pi = "graphs/" + "1000pfc100n5k" + f + "f/" + "1000pfc100n5k" + f + "f_" + "ord_pivot" + "_stats.pickle"
#     name_semi_ord_pi = "graphs/" + "1000pfc100n5k" + f + "f/" + "1000pfc100n5k" + f + "f_" + "semi_ord_pivot" + "_stats.pickle"
#     name_conc = "graphs/" + "1000pfc100n5k" + f + "f/" + "1000pfc100n5k" + f + "f_" + "concurrent" + "_stats.pickle"

#     print(data_analysis.get_average_stats(name_pivot))
#     print(data_analysis.get_average_stats(name_ord_pi))
#     print(data_analysis.get_average_stats(name_semi_ord_pi))
#     print(data_analysis.get_average_stats(name_conc))
#     print()


worst_graph_pivot = None
worst_ratio_pivot = 1.
worst_graph_conc = None
worst_ratio_conc = 1.
conc_over_two = []
pivot_over_two = []
biggest_ratio = 1
biggest_ratio_graph = None

for n in range(3,10):
    graphs = manage_files.load_object("graphs/all"+str(n)+"n/all"+str(n)+"n_graphs.pickle")
    stats_pivot = manage_files.load_object("graphs/all"+str(n)+"n/all"+str(n)+"n_pivot_stats.pickle")
    stats_conc = manage_files.load_object("graphs/all"+str(n)+"n/all"+str(n)+"n_concurrent_stats.pickle")
    opt_costs = manage_files.load_object("graphs/all"+str(n)+"n/all"+str(n)+"n_opt_cost.pickle")
    length = len(graphs)
    for i in range(length):
        mean_cost_pivot = stats_pivot[i][2]
        mean_cost_conc = stats_conc[i][2]
        opt_cost = opt_costs[i]
        if(mean_cost_pivot > biggest_ratio*mean_cost_conc):
            biggest_ratio = mean_cost_pivot/mean_cost_conc
            biggest_ratio_graph = graphs[i]
        if(mean_cost_conc > 1.6*opt_cost):
            conc_over_two.append((opt_cost,graphs[i],mean_cost_conc/opt_cost))
        if(mean_cost_pivot > 2*opt_cost):
            pivot_over_two.append((opt_cost,graphs[i],mean_cost_conc/opt_cost))
        if(mean_cost_pivot > worst_ratio_pivot*opt_cost):
            worst_ratio_pivot = mean_cost_pivot/opt_cost
            worst_graph_pivot = graphs[i]
            # print("pivot ", n, i, worst_ratio_pivot)
        if(mean_cost_conc > worst_ratio_conc * opt_cost):
            worst_ratio_conc = mean_cost_conc/opt_cost
            worst_graph_conc = graphs[i]
            # print("concurrent ", n, i, worst_ratio_conc)
        
# print("nb of graphs with mean concurrent cluster cost over 2*opt :",len(conc_over_two))
print("nb of graphs with mean pivot cost over 2*opt :",len(pivot_over_two))
print("biggest ratio", biggest_ratio)
print(biggest_ratio_graph)

# print(worst_graph_conc)
# print(worst_graph_pivot)
# print(conc_over_two)

# conc_over_two_bis = []
# for opt_cost, graph, ratio in conc_over_two:
#     size = graph.shape[0]
#     new_mean = np.mean(np.array([modele.clustering_cost(size, graph, algo.concurrent_clusters(size, graph)) for i in range(50)]))
#     if(new_mean > 1.7*opt_cost):
#         conc_over_two_bis.append((new_mean/opt_cost,graph))

# print("conc over 2 bis :",len(conc_over_two_bis))
# print(conc_over_two_bis)


# pivot_over_two_bis = []
# for opt_cost, graph, ratio in pivot_over_two:
#     size = graph.shape[0]
#     new_mean = np.mean(np.array([modele.clustering_cost(size, graph, algo.pivot(size, graph)) for i in range(75)]))
#     if(new_mean > 2*opt_cost):
#         pivot_over_two_bis.append((new_mean/opt_cost,graph))

# print("pivot over 2 bis :",len(pivot_over_two_bis))
# print(pivot_over_two_bis)


# conc_over_two_bis_bis = []
# for opt_cost, graph in conc_over_two_bis:
#     size = graph.shape[0]
#     new_mean = np.mean(np.array([modele.clustering_cost(size, graph, algo.concurrent_clusters(size, graph)) for i in range(50)]))
#     if(new_mean > 1.8*opt_cost):
#         conc_over_two_bis.append((new_mean/opt_cost,graph))

# print("conc over 2 bis bis :",len(conc_over_two_bis))
# print(conc_over_two_bis_bis)
from base import cities, cities_dict, connectionsA, connectionsB, distances, graph
from bfs import bfs_paths
from mst import build_graph, add_edges, minimum_spanning_tree, plot_graph, mst_total_weight
from greedy import greedy_paths

print("\n**************************************** CITIES' INFO *****************************************")
num_of_cities = 7
cities_coord = cities(num_of_cities)
cities_dictionary = cities_dict(cities_coord)

print("cities' coordinates:\n", cities_dictionary, "\n")

connections_a = connectionsA(cities_dictionary)
connections_b = connectionsB(connections_a)

distances_a = distances(connections_a, cities_dictionary)
distances_b = distances(connections_b, cities_dictionary)

print("possible connections between cities (scenario a):\n", connections_a, "\n")
print("possible connections between cities (scenario b):\n", connections_b, "\n")

print("distances between cities:\n", distances_a, "\n")

graph(cities_dictionary, distances_a)
graph(cities_dictionary, distances_b)

# BFS HERE!!!
print("\n*********************************************** BFS ***************************************************")

bfs_a, shortest_a = bfs_paths(connections_a, 0, num_of_cities, distances_a)
print("\npaths from city 0, scenario a:")
for i in bfs_a:
    print(i)
print("\nshortest path(s) in scenerio a: ", shortest_a)

bfs_b, shortest_b = bfs_paths(connections_b, 0, num_of_cities, distances_b)
print("\npaths from city 0, scenario b:")
for i in bfs_b:
    print(i)
print("\nshortest path(s) in scenario b: ", shortest_b)

#  MST HERE!!!
print("\n*********************************************** MST ***************************************************")

graph_a = build_graph(cities_dictionary, 0)
add_edges(graph_a, connections_a, distances_a)
mst_a = minimum_spanning_tree(graph_a)
print("\nminimum spanning tree weight (scenario a):", mst_total_weight(mst_a))
plot_graph(mst_a)

graph_b = build_graph(cities_dictionary, 0)
add_edges(graph_b, connections_b, distances_b)
mst_b = minimum_spanning_tree(graph_b)
print("\nminimum spanning tree weight (scenario b):", mst_total_weight(mst_b))
plot_graph(mst_b)

# GREEDY HERE!!!
print("\n********************************************** GREEDY **************************************************")
greedy_path_a, greedy_cost_a = greedy_paths(connections_a, 0, num_of_cities, distances_a)
print("\ngreedy path (scenario a):", greedy_path_a)
print("greedy cost (scenario a):", greedy_cost_a)
greedy_path_b, greedy_cost_b = greedy_paths(connections_b, 0, num_of_cities, distances_b)
print("\ngreedy path (scenario b):", greedy_path_b)
print("greedy cost (scenario b):", greedy_cost_b)

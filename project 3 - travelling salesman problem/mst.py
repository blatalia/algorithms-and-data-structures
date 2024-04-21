import networkx as nx
import matplotlib.pyplot as plt

def build_graph(cities, start_city):
    graph = nx.Graph()
    for city_index, pos in cities.items():
        graph.add_node(city_index, pos=pos)
    graph.add_edge(start_city, start_city, weight=0)
    return graph

def add_edges(graph, connections, distances):
    for connection in connections:
        city1, city2 = connection
        distance = distances[connection]
        graph.add_edge(city1, city2, weight=distance)
        graph.add_edge(city2, city1, weight=distance)

def minimum_spanning_tree(graph):
    mst = nx.minimum_spanning_tree(graph)
    return mst

def plot_graph(graph):
    pos = nx.get_node_attributes(graph, 'pos')
    nx.draw(graph, pos, with_labels=True, node_size=200, font_size=8)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

def mst_total_weight(mst):
    total_weight = 0
    for edge in mst.edges.data():
        total_weight += edge[2]['weight']
    return total_weight


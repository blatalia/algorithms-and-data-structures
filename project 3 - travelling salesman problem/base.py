import random
import numpy as np
from itertools import combinations
import matplotlib.pyplot as plt

def cities(a):
    cities = []
    for i in range(a):
        cities.append((random.randint(-100, 100), random.randint(-100, 100)))
    return cities

def cities_dict(cities):
    cities_dict = {}
    for count, value in enumerate(cities):
        cities_dict[count] = value
    return cities_dict

def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def connectionsA(cities_coord):
    connectionsA = list(combinations(cities_coord.keys(), 2))
    return connectionsA

def connectionsB(citiesA):
    connectionsB = citiesA.copy()
    for i in range(len(citiesA)):
        if random.random() > 0.8:
            connectionsB.remove(citiesA[i])
    return connectionsB

def distances(connections, cities_dict):
    distances = {}
    for connection in connections:
        city1, city2 = connection
        distance = calculate_distance(cities_dict[city1], cities_dict[city2])
        distances[connection] = distance
    return distances

def get_neighbors(connections, node):
    neighbors = []
    for connection in connections:
        if connection[0] == node:
            neighbors.append(connection[1])
        elif connection[1] == node:
            neighbors.append(connection[0])
    return neighbors

def graph(cities_dict, distances):
    plt.figure()
    for city, coord in cities_dict.items():
        plt.scatter(coord[0], coord[1], s=200)
        plt.text(coord[0], coord[1], city, ha='center', va='bottom')
    
    for (city1, city2), dist in distances.items():
        city1_coord = cities_dict[city1]
        city2_coord = cities_dict[city2]
        plt.plot([city1_coord[0], city2_coord[0]], [city1_coord[1], city2_coord[1]], color='black', alpha=0.5)
        mid_x = (city1_coord[0] + city2_coord[0]) / 2
        mid_y = (city1_coord[1] + city2_coord[1]) / 2
        plt.text(mid_x, mid_y, f"{dist:.2f}", ha='center', va='top')

    plt.xticks([])
    plt.yticks([])
    plt.title("Weighted Graph")
    plt.show()

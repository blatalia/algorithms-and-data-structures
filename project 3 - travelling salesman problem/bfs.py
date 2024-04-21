from base import get_neighbors
from collections import deque
# BFS HERE!!!
def bfs_paths(connections, start_node, num_of_cities, distances):
    queue = deque([[start_node]])
    paths_and_costs = []
    shortest_paths = []
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        neighbors = get_neighbors(connections, node)
        
        for neighbor in neighbors:
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append(new_path)
                
                if len(new_path) == num_of_cities and start_node in get_neighbors(connections, neighbor):
                    new_path += [start_node]
                    cost = 0
                    for x in range(1, len(new_path)):
                        connection = tuple(sorted([new_path[x-1], new_path[x]]))
                        cost += distances.get(connection, 0)
                    
                    paths_and_costs.append((new_path, cost))

    cheapest = paths_and_costs[0][1]
    for path, cost in paths_and_costs:
        if cost < cheapest:
            cheapest = cost
            
    for path, cost in paths_and_costs:
        if cost == cheapest:
            shortest_paths.append((path, cost))
            
    return paths_and_costs, shortest_paths



from base import get_neighbors

def greedy_paths(connections, start_node, num_of_cities, distances):
    path = [start_node]
    current_node = start_node
    neighbors = get_neighbors(connections, current_node)
    cost = 0

    while len(path) < num_of_cities:
        cheapest = None
        min_distance = float('inf')
        
        for neighbor in neighbors:
            if neighbor not in path:
                connection = tuple(sorted([current_node, neighbor]))
                distance = distances.get(connection, float('inf'))
                if distance < min_distance:
                    cheapest = neighbor
                    min_distance = distance

        if cheapest is None:
            break

        path.append(cheapest)
        cost += min_distance
        current_node = cheapest
        neighbors = get_neighbors(connections, current_node)

    return path, cost
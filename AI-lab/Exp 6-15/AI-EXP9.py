from itertools import permutations

def tsp(graph, start):
    cities = [city for city in graph if city != start]
    min_cost = float('inf')
    best_route = None

    for route in permutations(cities):
        path = (start,) + route + (start,)
        cost = 0

        for i in range(len(path) - 1):
            cost += graph[path[i]][path[i + 1]]

        if cost < min_cost:
            min_cost = cost
            best_route = path

    print("Best Route:", " -> ".join(best_route))
    print("Minimum Cost:", min_cost)

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

tsp(graph, 'A')
import heapq

def astar(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if node == goal:
            print("Shortest Path:", " -> ".join(path))
            print("Total Cost:", cost)
            return

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                new_cost = cost + weight
                new_f = new_cost + heuristic[neighbor]
                heapq.heappush(
                    pq, (new_f, new_cost, neighbor,
                         path + [neighbor])
                )

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'E': 1},
    'D': {'G': 5},
    'E': {'G': 3},
    'G': {}
}

heuristic = {
    'A': 7, 'B': 6, 'C': 4,
    'D': 4, 'E': 2, 'G': 0
}

astar(graph, heuristic, 'A', 'G')
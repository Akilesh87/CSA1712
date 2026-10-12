def color_map(graph, colors):
    result = {}

    def solve(node):
        if node == len(graph):
            return True

        region = list(graph.keys())[node]

        for color in colors:
            safe = True

            for neighbor in graph[region]:
                if result.get(neighbor) == color:
                    safe = False
                    break

            if safe:
                result[region] = color

                if solve(node + 1):
                    return True

                del result[region]

        return False

    if solve(0):
        print("Map Coloring:")
        for region, color in result.items():
            print(region, ":", color)
    else:
        print("No solution exists.")

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
color_map(graph, colors)
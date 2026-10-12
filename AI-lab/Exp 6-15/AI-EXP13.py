def minimax(depth, node, maximizing, scores):
    if depth == 2:
        return scores[node]

    if maximizing:
        best = float('-inf')

        for i in range(2):
            best = max(best, minimax(
                depth + 1, node * 2 + i, False, scores
            ))

        return best

    else:
        best = float('inf')

        for i in range(2):
            best = min(best, minimax(
                depth + 1, node * 2 + i, True, scores
            ))

        return best

scores = [3, 5, 2, 9]

print("Best value:", minimax(0, 0, True, scores))
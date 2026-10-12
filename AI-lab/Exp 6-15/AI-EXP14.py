def alphabeta(depth, node, maximizing, scores, alpha, beta):
    if depth == 2:
        return scores[node]

    if maximizing:
        best = float('-inf')

        for i in range(2):
            value = alphabeta(
                depth + 1, node * 2 + i,
                False, scores, alpha, beta
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            value = alphabeta(
                depth + 1, node * 2 + i,
                True, scores, alpha, beta
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

scores = [3, 5, 2, 9]

result = alphabeta(
    0, 0, True, scores,
    float('-inf'), float('inf')
)

print("Best value:", result)
def alpha_beta(depth, node_index, is_max, scores, height, alpha, beta):

    if depth >= height:
        return scores[node_index]

    if is_max:
        best = -999999
        val = alpha_beta(depth + 1, node_index * 2, False, scores, height, alpha, beta)
        best = max(best, val)
        alpha = max(alpha, best)

        if beta <= alpha:
            return best

        val = alpha_beta(depth + 1, node_index * 2 + 1, False, scores, height, alpha, beta)
        best = max(best, val)
        return best

    else:
        best = 999999
        val = alpha_beta(depth + 1, node_index * 2, True, scores, height, alpha, beta)
        best = min(best, val)
        beta = min(beta, best)

        if beta <= alpha:
            return best

        val = alpha_beta(depth + 1, node_index * 2 + 1, True, scores, height, alpha, beta)
        best = min(best, val)
        return best


# Main Program
scores = list(map(int, input("Enter the values of the leaf nodes: ").split()))

height = 3

result = alpha_beta(0, 0, True, scores, height, -999999, 999999)

print("\nThe optimal value is:", result)

#output
# Enter the values of the leaf nodes: 3 5 2 9 12 5 23 23
# 
# The optimal value is: 12
def minimax(depth, node_index, is_max, scores, height):

    if depth >= height:
        return scores[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        )

    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        )


# Main Program
scores = list(map(int, input("Enter the values of the leaf nodes: ").split()))

height = 3

result = minimax(0, 0, True, scores, height)

print("\nThe optimal value is:", result)

#output
# Enter the values of the leaf nodes: 3 5 2 9 12 5 23 23
# 
# The optimal value is: 12
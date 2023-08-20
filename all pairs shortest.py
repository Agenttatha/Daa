def compute_shortest_paths(adjacency_matrix):
    n = len(adjacency_matrix)

    # Initialize the distance matrix with the adjacency matrix
    # distance_matrix = [[adjacency_matrix[i][j] for j in range(n)] for i in range(n)]
    # print(distance_matrix)

    # Compute the shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])

    return adjacency_matrix
adjacency_matrix = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]

shortest_paths = compute_shortest_paths(adjacency_matrix)
for row in shortest_paths:
    print(row)

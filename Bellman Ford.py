def calculate_minimum_wire_length(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0

    for _ in range(n - 1):
        for node in range(n):
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


graph = [
    # 0   [(1, 3), (2, 4), (3, 2)],
    # 1 [(0, 3), (2, 2)],
    # 2 [(0, 4), (1, 2), (3, 1)],
    # 3 [(0, 2), (2, 1)]
]
device = 0  # The device to calculate the minimum wire length for

distances = calculate_minimum_wire_length(graph, device)
print(
    f"The minimum wire lengths to connect device {device} to all other devices are: {distances}")

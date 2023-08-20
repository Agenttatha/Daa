import heapq


def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor_node, weight in graph[current_node]:

            distance = current_distance + weight

            if distance < distances[neighbor_node]:
                distances[neighbor_node] = distance
                heapq.heappush(heap, (distance, neighbor_node))

    print(distances)

    return distances


def minimum_wire_length(graph, device1, device2):
    distances = dijkstra(graph, device1)
    return distances[device2]


# Example usage
graph = [
    [(1, 3), (2, 4), (3, 2)],
    [(0, 3), (2, 2)],
    [(0, 4), (1, 2), (3, 1)],
    [(0, 2), (2, 1)]
]

device1 = 3
device2 = 3

minimum_length = minimum_wire_length(graph, device1, device2)
print(
    f"The minimum length of wire required to connect device {device1} and device {device2} is: {minimum_length}")

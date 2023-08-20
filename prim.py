import heapq


def minimum_wire_length(N, connections):
    graph = [[] for _ in range(N)]

    for D1, D2, L in connections:
        graph[D1].append((D2, L))
        graph[D2].append((D1, L))

    visited = [False] * N
    min_heap = [(0, 0)]  # (length, device)

    total_length = 0

    while min_heap:
        length, device = heapq.heappop(min_heap)

        if visited[device]:
            continue

        visited[device] = True
        total_length += length

        for neighbor, neighbor_length in graph[device]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (neighbor_length, neighbor))

    return total_length


def main():
    # Example input
    N = 5  # Number of devices
    connections = [
        (0, 1, 2),  # D0 connected to D1 with wire length 2
        (0, 2, 3),  # D0 connected to D2 with wire length 3
        (1, 3, 1),  # D1 connected to D3 with wire length 1
        (2, 3, 4),  # D2 connected to D3 with wire length 4
        (2, 4, 5),  # D2 connected to D4 with wire length 5
    ]

    minimum_length = minimum_wire_length(N, connections)
    print("Minimum length of wire required:", minimum_length)


if __name__ == "__main__":
    main()

from collections import defaultdict

class PowerGridGraph:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.adj_list = defaultdict(list)
        self.visited = [False] * num_cities
        self.disc = [0] * num_cities
        self.low = [0] * num_cities
        self.time = 0
        self.articulation_points = set()

    def add_connection(self, city1, city2):
        self.adj_list[city1].append(city2)
        self.adj_list[city2].append(city1)

    def is_bi_connected(self):
        # Check if the graph is connected
        if not self.is_connected():
            return False

        # Initialize visited, discovery time, and low value arrays
        self.visited = [False] * self.num_cities
        self.disc = [0] * self.num_cities
        self.low = [0] * self.num_cities

        # Perform a Depth-First Search from the first city
        self.is_bi_connected_util(0, -1)

        return len(self.articulation_points) == 0

    def is_bi_connected_util(self, current_city, parent):
        # Mark the current city as visited
        self.visited[current_city] = True

        # Initialize discovery time and low value for the city
        self.disc[current_city] = self.time
        self.low[current_city] = self.time
        self.time += 1

        # Count the number of children in the DFS tree
        children = 0

        # Iterate through all adjacent cities of the current city
        for next_city in self.adj_list[current_city]:
            if not self.visited[next_city]:
                children += 1
                self.is_bi_connected_util(next_city, current_city)

                # Update the low value of the current city
                self.low[current_city] = min(self.low[current_city], self.low[next_city])

                # Check if the current city is an articulation point
                if parent != -1 and self.low[next_city] >= self.disc[current_city]:
                    self.articulation_points.add(current_city)
                if parent == -1 and children > 1:
                    self.articulation_points.add(current_city)
            elif next_city != parent:
                # Update the low value of the current city for the back edge
                self.low[current_city] = min(self.low[current_city], self.disc[next_city])

    def is_connected(self):
        # Perform a Depth-First Search to check if the graph is connected
        self.visited = [False] * self.num_cities
        self.dfs(0)
        return all(self.visited)

    def dfs(self, current_city):
        self.visited[current_city] = True
        for next_city in self.adj_list[current_city]:
            if not self.visited[next_city]:
                self.dfs(next_city)

    def print_articulation_points(self):
        if len(self.articulation_points) > 0:
            print("Articulation Points:")
            for point in self.articulation_points:
                print(point)
        else:
            print("No articulation points found.")

# Example usage
power_grid = PowerGridGraph(3)
power_grid.add_connection(0, 1)
power_grid.add_connection(1, 2)
power_grid.add_connection(2, 0)

if power_grid.is_bi_connected():
    print("The power grid network is bi-connected.")
else:
    print("The power grid network is not bi-connected.")

power_grid.print_articulation_points()

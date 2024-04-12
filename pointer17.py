import heapq

def travel_time(distance, speed):

    return (distance / speed) * 60

def min_time_and_cost():

    nodes = [0, 1, 2, 3, 4, 5]  # 0km, 1km, 5km, 10km, 25km, 30km marks
    distances = [1, 4, 5, 15, 5]  # Distances between consecutive nodes
    graph = {i: [] for i in nodes}

    # Populate graph with edges for each travel mode with waiting times
    for i in range(len(distances)):
        walk_time = travel_time(distances[i], 5)
        bus_time = travel_time(distances[i], 30) + 8
        taxi_time = travel_time(distances[i], 50) + 4

        bus_cost = 1 + 0.01 * distances[i]
        taxi_cost = 4 + 0.20 * distances[i]

        # Adding edges for each mode
        graph[i].append((walk_time, 0, i+1))  # include walking
        if i < len(distances):
            if bus_cost <= 8:
                graph[i].append((bus_time, bus_cost, i+1))
            if taxi_cost <= 8:
                graph[i].append((taxi_time, taxi_cost, i+1))

    # priority queue using quasi-dijkstra traversal
    priority_queue = [(0, 0, 0)]  # (current_time, current_cost, current_node)
    visited = set()
    previous_nodes = {0: None}  # create a dict

    while priority_queue:
        current_time, current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == 5:  # Reached office
            # backtrack to get the exact route
            route = [] 
            while current_node is not None:
                route.append(current_node)
                current_node = previous_nodes[current_node]
            route.reverse()
            return current_time, current_cost, route

        if current_node in visited:
            continue
        visited.add(current_node)

        for time, cost, next_node in graph[current_node]:
            next_time = current_time + time
            next_cost = current_cost + cost
            if next_cost <= 8 and next_node not in visited:  # Check budget and unvisited
                heapq.heappush(priority_queue, (next_time, next_cost, next_node))
                previous_nodes[next_node] = current_node  # Update node

    return None

# Example usage
result = min_time_and_cost()
if result:
    fastest_time, total_cost, route = result
    print(f"Fastest time: {fastest_time} minutes with a cost of ${total_cost:.2f}")
    print(f"Route: {route}")
else:
    print("No feasible path found within the budget.")

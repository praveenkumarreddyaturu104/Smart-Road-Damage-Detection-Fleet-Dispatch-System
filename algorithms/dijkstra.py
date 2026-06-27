"""
Implement Dijkstra algorithm and route planning for road repairs.
"""

import heapq


def dijkstra(graph, start_node):
    """
    Standard Dijkstra's algorithm.
    Finds the shortest distance from start_node to all other nodes in the graph.
    Returns: distances dict
    """
    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0
    
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph.get(current_node, []):
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
                
    return distances


def dijkstra_path(graph, start_node, end_node):
    """
    Finds the shortest path and total distance between start_node and end_node.
    Returns: (path list, distance float)
    """
    # Track distances and predecessors
    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0
    predecessors = {node: None for node in graph}
    
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == end_node:
            break
            
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph.get(current_node, []):
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))
                
    # Reconstruct path
    path = []
    curr = end_node
    while curr is not None:
        path.append(curr)
        curr = predecessors[curr]
    path.reverse()
    
    if distances[end_node] == float("inf"):
        return [], float("inf")
        
    return path, distances[end_node]


def calculate_multi_stop_route(graph, start_node, stops):
    """
    Calculate the shortest route starting at start_node, visiting all stops in sequence,
    and returning back to start_node.
    Returns: (full_path list, total_distance float)
    """
    if not stops:
        return [start_node], 0.0
        
    full_path = [start_node]
    total_distance = 0.0
    current_start = start_node
    
    # Visit each stop sequentially
    for stop in stops:
        path, dist = dijkstra_path(graph, current_start, stop)
        if dist == float("inf"):
            return [], float("inf")
        # Append path, skipping the first element (which is the current_start)
        full_path.extend(path[1:])
        total_distance += dist
        current_start = stop
        
    # Return to starting point
    path, dist = dijkstra_path(graph, current_start, start_node)
    if dist == float("inf"):
        return [], float("inf")
    full_path.extend(path[1:])
    total_distance += dist
    
    return full_path, total_distance


# Pre-defined city road network for simulation.
# Nodes represent the central Repair Center (Depot) and different city sectors.
ROAD_NETWORK = {
    "Repair Center": [("Sector Alpha", 4), ("Sector Gamma", 3)],
    "Sector Alpha": [("Repair Center", 4), ("Sector Beta", 5), ("Sector Delta", 6)],
    "Sector Beta": [("Sector Alpha", 5), ("Sector Delta", 2), ("Sector Epsilon", 7)],
    "Sector Gamma": [("Repair Center", 3), ("Sector Delta", 4), ("Sector Epsilon", 8)],
    "Sector Delta": [("Sector Alpha", 6), ("Sector Beta", 2), ("Sector Gamma", 4), ("Sector Epsilon", 3)],
    "Sector Epsilon": [("Sector Beta", 7), ("Sector Gamma", 8), ("Sector Delta", 3)]
}
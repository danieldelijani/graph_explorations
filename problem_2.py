import random
import heapq
from collections import defaultdict

def average_degree(edges):
    """Returns the average degree for verticies in the graph."""
    num_neighbors = defaultdict(int)
    for edge in edges:
        num_neighbors[edge[0]] += 1
        num_neighbors[edge[1]] += 1
    return float(sum(num_neighbors.values())) / len(num_neighbors)

def get_euclidean_distance(point1, point2):
    """Returns the euclidean distance of two points in R2."""
    return (((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2)) ** .5

def generate_graph_1(n, d):
    """Generates a graph consisting of n verticies with roughly degree d."""
    def get_closest_points(vertex):
        """gets the d closest points to a vertex"""
        vertex_value = vertex_location_map[vertex]
        distance_vertex = []
        for other_vertex in range(n):
            if other_vertex == vertex: continue
            distance_vertex.append((get_euclidean_distance(vertex_value, vertex_location_map[other_vertex]), other_vertex))

        closest_points = heapq.nsmallest(d, distance_vertex)
        return [point for distance, point in closest_points]

    vertex_location_map = {vertex:(random.random(), random.random()) for vertex in range(n)}
    edges = []
    already_added_edges = set() # to handle parallel edges in O(1) time
    for vertex in range(n):
        neighbors = get_closest_points(vertex)
        for neigh in neighbors:
            if ((vertex, neigh) not in already_added_edges) and ((neigh, vertex) not in already_added_edges):
                edges.append((vertex, neigh))
                already_added_edges.add((vertex, neigh))
    return edges

def generate_graph_2(n, d):
    """Generates a graph consisting of n verticies with roughly degree d with Erdős-Rényi model."""
    # calculate probability of an edge between two nodes
    p = d / (n - 1)

    # create empty graph
    edges = []

    # generate edges with probability p
    for node_1 in range(n):
        for node_2 in range(node_1 + 1, n):
            if random.random() < p:
                edges.append((node_1, node_2))
    return edges

if __name__ == '__main__':
    graph = generate_graph_1(1000, 7)
    print(average_degree(graph))

    graph = generate_graph_2(1000, 7)
    print(average_degree(graph))
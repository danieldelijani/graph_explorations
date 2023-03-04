import random
import heapq
from collections import defaultdict

def average_degree(graph):
    """Returns the average degree for verticies in the graph."""
    lengths = [len(neighs) for neighs in graph.values()]
    return sum(lengths) / len(lengths)

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
    graph = defaultdict(list)
    for vertex in range(n):
        neighbors = get_closest_points(vertex)
        for neigh in neighbors:
            graph[vertex].append(neigh)
            graph[neigh].append(vertex)
    return graph

def generate_graph_2(n, d):
    """Generates a graph consisting of n verticies with roughly degree d."""
    # TODO(implement this)
    pass

if __name__ == '__main__':
    graph = generate_graph_1(100, 7)
    print(graph)
    print(average_degree(graph))

    # graph = generate_graph_2(100, 7)
    # print(graph)
    # print(average_degree(graph))
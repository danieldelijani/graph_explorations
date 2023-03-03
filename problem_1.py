import random
import copy
from collections import defaultdict

def algorithm1(edges):
    random.shuffle(edges)
    M = set()
    edges_in_m = set()
    for edge in edges:
        if (edge[0] not in edges_in_m) and (edge[1] not in edges_in_m):
            M.add(edge)
            edges_in_m.add(edge[0])
            edges_in_m.add(edge[1])
    return M

def algorithm2(edges):
    def selected1(e):
        node_1 = e[0]
        node_2 = e[1]
        selected = True
        adjacent_edges = graph[node_1].union(graph[node_2]).difference(set([e]))
        for adjacent_edge in adjacent_edges:
            if edge_r_map[adjacent_edge] < edge_r_map[e]:
                if selected1(adjacent_edge):
                    selected = False
        return selected
    
    # create hashmap {node -> edges with node as an endpoint}
    graph = defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge)
        graph[edge[1]].add(edge)

    # define maximum matching set
    M = set()

    # create random numbers for each edge
    edge_r_map = {e:random.random() for e in edges}

    for edge in edges:
        if selected1(edge):
            M.add(edge)
    return M

def algorithm3(edges):
    def selected2(e):
        node_1 = e[0]
        node_2 = e[1]
        adjacent_edges = graph[node_1].union(graph[node_2]).difference(set([e]))
        for adjacent_edge in adjacent_edges:
            if edge_r_map[adjacent_edge] < edge_r_map[e]:
                if selected2(adjacent_edge):
                    return False
        return True
    
    # create hashmap {node -> edges with node as an endpoint}
    graph = defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge)
        graph[edge[1]].add(edge)

    # define maximum matching set
    M = set()

    # create random numbers for each edge
    edge_r_map = {e:random.random() for e in edges}

    for edge in edges:
        if selected2(edge):
            M.add(edge)
    return M

def algorithm4(edges):
    def selected3(e):
        node_1 = e[0]
        node_2 = e[1]
        adjacent_edges = graph[node_1].union(graph[node_2]).difference(set([e]))
        sorted_adjacent_edges = sorted(adjacent_edges, key=lambda edge: edge_r_map[edge])
        for adjacent_edge in sorted_adjacent_edges:
            if edge_r_map[adjacent_edge] < edge_r_map[e]:
                if selected3(adjacent_edge):
                    return False
        return True
    
    # create hashmap {node -> edges with node as an endpoint}
    graph = defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge)
        graph[edge[1]].add(edge)

    # define maximum matching set
    M = set()

    # create random numbers for each edge
    edge_r_map = {e:random.random() for e in edges}

    for edge in edges:
        if selected3(edge):
            M.add(edge)
    return M

def algorithm5(edges):
    def selected4(e):
        # TODO(use LRU Cache)
        node_1 = e[0]
        node_2 = e[1]
        adjacent_edges = graph[node_1].union(graph[node_2]).difference(set([e]))
        sorted_adjacent_edges = sorted(adjacent_edges, key=lambda edge: edge_r_map[edge])
        for adjacent_edge in sorted_adjacent_edges:
            if edge_r_map[adjacent_edge] < edge_r_map[e]:
                if selected4(adjacent_edge):
                    return False
        return True
        
    # create hashmap {node -> edges with node as an endpoint}
    graph = defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge)
        graph[edge[1]].add(edge)

    # define maximum matching set
    M = set()

    # create random numbers for each edge
    edge_r_map = {e:random.random() for e in edges}

    for edge in edges:
        if selected4(edge):
            M.add(edge)
    return M


# define some test data
TEST_EDGES = [(1, 2), (2, 3), (5, 2), (3, 4), (6, 3), (4, 5)]
print(algorithm1(copy.deepcopy(TEST_EDGES)))
print(algorithm2(copy.deepcopy(TEST_EDGES)))
print(algorithm3(copy.deepcopy(TEST_EDGES)))
print(algorithm4(copy.deepcopy(TEST_EDGES)))
print(algorithm5(copy.deepcopy(TEST_EDGES)))


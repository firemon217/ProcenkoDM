from graph_representation import Graph
import heapq
from grapsh_traversal import dfs_recursive

def connected_components(graph: Graph):
    visited = set()
    components = []

    for v in graph.get_vertices():
        if v not in visited:
            order = dfs_recursive(graph, v)
            for u in order:
                visited.add(u)
            components.append(order)

    return components

def topological_sort(graph: Graph):
    visited = set()
    result = []

    def dfs_topo(v):
        visited.add(v)
        for u, _ in graph.neighbors(v):
            if u not in visited:
                dfs_topo(u)
        result.append(v)

    for v in graph.get_vertices():
        if v not in visited:
            dfs_topo(v)

    result.reverse()
    return result

def dijkstra(graph: Graph, start):
    vertices = graph.get_vertices()
    dist = {v: float('inf') for v in vertices}
    parent = {v: None for v in vertices}
    dist[start] = 0

    pq = [(0, start)]
    while pq:
        d, v = heapq.heappop(pq)
        if d != dist[v]:
            continue
        for u, w in graph.neighbors(v):
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                parent[u] = v
                heapq.heappush(pq, (dist[u], u))

    return dist, parent

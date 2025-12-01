from graph_representation import Graph
from collections import deque

def bfs(graph: Graph, start):
    vertices = graph.get_vertices()
    dist = {v: float('inf') for v in vertices}
    parent = {v: None for v in vertices}

    queue = deque([start])
    dist[start] = 0

    while queue:
        u = queue.popleft()
        for v, _ in graph.neighbors(u):
            if dist[v] == float('inf'):
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)

    def build_path(to):
        if dist[to] == float('inf'):
            return None
        path = []
        while to is not None:
            path.append(to)
            to = parent[to]
        return list(reversed(path))

    return dist, parent, build_path

def dfs_recursive(graph: Graph, start):
    visited = set()
    order = []

    def dfs(v):
        visited.add(v)
        order.append(v)
        for u, _ in graph.neighbors(v):
            if u not in visited:
                dfs(u)

    dfs(start)
    return order

def dfs_iterative(graph: Graph, start):
    visited = set()
    order = []
    stack = [start]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            order.append(v)
            for u, _ in reversed(graph.neighbors(v)):
                if u not in visited:
                    stack.append(u)
    return order
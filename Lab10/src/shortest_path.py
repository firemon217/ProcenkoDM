import heapq
from graph_traversal import dfs_recursive

def connected_components(graph):
    """
    Находит компоненты связности
    Время: O(V + E)
    Память: O(V)
    """
    visited = set()
    components = []

    for vertex in graph.graph:
        if vertex not in visited:
            component = dfs_recursive(graph, vertex)
            components.append(component)
            visited.update(component)
    return components

def topological_sort(graph):
    """
    Топологическая сортировка DAG
    Время: O(V + E)
    Память: O(V)
    """
    visited = set()
    stack = []

    def dfs(u):
        visited.add(u)
        for v, _ in graph.graph.get(u, []):
            if v not in visited:
                dfs(v)
        stack.append(u)

    for vertex in graph.graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]

def dijkstra(graph, start):
    """
    Находит кратчайшие пути из start
    Время: O((V + E) log V) с кучей
    Память: O(V)
    """
    distances = {v: float('inf') for v in graph.graph}
    distances[start] = 0
    pq = [(0, start)]
    parents = {start: None}

    while pq:
        current_distance, u = heapq.heappop(pq)
        if current_distance > distances[u]:
            continue
        for v, weight in graph.graph.get(u, []):
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                parents[v] = u
                heapq.heappush(pq, (distance, v))
    return distances, parents

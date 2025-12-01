from collections import deque

def bfs(graph, start):
    """
    Breadth-First Search
    Возвращает: расстояния и родительские вершины
    Время: O(V + E)
    Память: O(V)
    """
    visited = set()
    queue = deque([start])
    distances = {start: 0}
    parents = {start: None}

    while queue:
        u = queue.popleft()
        visited.add(u)
        for v, _ in graph.graph.get(u, []):
            if v not in visited and v not in queue:
                queue.append(v)
                distances[v] = distances[u] + 1
                parents[v] = u
    return distances, parents

def dfs_recursive(graph, start, visited=None):
    """
    Depth-First Search рекурсивный
    Время: O(V + E)
    Память: O(V) для стека рекурсии
    """
    if visited is None:
        visited = set()
    visited.add(start)
    for v, _ in graph.graph.get(start, []):
        if v not in visited:
            dfs_recursive(graph, v, visited)
    return visited

def dfs_iterative(graph, start):
    """
    Depth-First Search итеративный через стек
    Время: O(V + E)
    Память: O(V)
    """
    visited = set()
    stack = [start]

    while stack:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            for v, _ in graph.graph.get(u, []):
                if v not in visited:
                    stack.append(v)
    return visited

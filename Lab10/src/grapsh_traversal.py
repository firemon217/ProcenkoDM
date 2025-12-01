from collections import deque

def bfs(graph, start):
    """
    BFS с возвращением расстояний и путей.
    Сложность: O(V + E) — каждая вершина и каждое ребро посещаются один раз.
    """

    dist = {v: float('inf') for v in graph.adj}
    parent = {v: None for v in graph.adj}

    queue = deque([start])
    dist[start] = 0

    while queue:
        u = queue.popleft()
        for v in graph.adj[u]:
            if dist[v] == float('inf'):  # не посещён
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)
    
    # Функция восстановления пути
    def build_path(to):
        if dist[to] == float('inf'):
            return None
        path = []
        while to is not None:
            path.append(to)
            to = parent[to]
        return list(reversed(path))

    return dist, parent, build_path

def dfs_recursive(graph, start):
    """
    Рекурсивный DFS.
    Сложность:
        O(V + E) — каждое ребро и вершина посещаются один раз.
    """

    visited = set()
    order = []

    def dfs(v):
        visited.add(v)
        order.append(v)
        for u in graph.adj[v]:
            if u not in visited:
                dfs(u)

    dfs(start)
    return order

def dfs_iterative(graph, start):
    """
    Итеративный DFS (вариант с собственным стеком).
    Сложность:
        O(V + E)
    """

    visited = set()
    order = []

    stack = [start]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            order.append(v)
            # Обратный порядок, чтобы первый сосед обрабатывался первым
            for u in reversed(graph.adj[v]):
                if u not in visited:
                    stack.append(u)

    return order

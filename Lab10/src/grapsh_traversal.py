from collections import deque   # импорт двусторонней очереди для BFS

def bfs(graph, start):
    """
    BFS с возвращением расстояний и путей.
    Сложность: O(V + E)
    """

    vertices = graph.get_vertices()   # получаем список всех вершин графа

    dist = {v: float('inf') for v in vertices}  # словарь расстояний: изначально бесконечность
    parent = {v: None for v in vertices}        # словарь родителей

    queue = deque([start])      # создаём очередь и кладём в неё стартовую вершину
    dist[start] = 0             # расстояние от стартовой вершины до себя = 0

    while queue:                # пока очередь не пуста
        u = queue.popleft()     # извлекаем вершину из начала очереди

        for v in graph.neighbors(u):        # проходим по каждому соседу текущей вершины u
            if dist[v] == float('inf'):     # если сосед ещё не посещён
                dist[v] = dist[u] + 1       # обновляем расстояние до него
                parent[v] = u               # запоминаем, откуда пришли
                queue.append(v)             # добавляем соседа в очередь

    def build_path(to):             # вложенная функция восстановления пути
        if dist[to] == float('inf'):
            return None
        path = []                   # список для хранения пути
        while to is not None:       # поднимаемся по родителям вверх
            path.append(to)
            to = parent[to]
        return list(reversed(path))   # путь восстановлен в обратном порядке

    return dist, parent, build_path    # возвращаем расстояния, родителей и функцию пути
    # Сложность: O(V + E) — каждая вершина и каждое ребро обрабатываются один раз.

def dfs_recursive(graph, start):
    """
    Рекурсивный DFS.
    Сложность: O(V + E)
    """
    visited = set()      # множество посещённых вершин
    order = []           # порядок обхода

    def dfs(v):                  # рекурсивная функция обхода
        visited.add(v)           # помечаем вершину как посещённую
        order.append(v)          # добавляем в порядок посещения

        for u in graph.neighbors(v):   # перебираем всех соседей вершины v
            if u not in visited:       # если сосед не посещён
                dfs(u)                 # вызываем DFS от него

    dfs(start)      # запускаем обход с заданной стартовой вершины
    return order    # возвращаем порядок посещения вершин
    # Сложность: O(V + E) — один обход графа, глубина рекурсии до V.

def dfs_iterative(graph, start):
    """
    Итеративный DFS.
    Сложность: O(V + E)
    """
    visited = set()       # множество посещённых вершин
    order = []            # порядок обхода
    stack = [start]       # собственный стек, вместо рекурсивного

    while stack:                  # пока стек не пуст
        v = stack.pop()           # извлекаем вершину с вершины стека

        if v not in visited:      # обрабатываем только непосещённые
            visited.add(v)        # помечаем вершину как посещённую
            order.append(v)       # добавляем в порядок посещения

            for u in reversed(graph.neighbors(v)):  # соседей кладём в стек
                if u not in visited:                # только непосещённые
                    stack.append(u)                 # кладём в стек

    return order        # возвращаем порядок обхода
    # Сложность: O(V + E) — как рекурсивный DFS, но без рекурсии.

from collections import deque
import heapq

class Graph:
    """Базовый абстрактный класс графа."""
    
    def add_vertex(self, v):
        """Добавление вершины."""
        raise NotImplementedError

    def remove_vertex(self, v):
        """Удаление вершины."""
        raise NotImplementedError

    def add_edge(self, u, v, weight=1):
        """Добавление ребра с весом."""
        raise NotImplementedError

    def remove_edge(self, u, v):
        """Удаление ребра."""
        raise NotImplementedError

    def neighbors(self, v):
        """Возвращает список соседей вершины.
        Для Дейкстры: возвращает (vertex, weight)
        """
        raise NotImplementedError

    def get_vertices(self):
        """Возвращает список всех вершин графа."""
        raise NotImplementedError

class AdjacencyMatrix(Graph):
    def __init__(self, n=0):
        """Создание матрицы смежности для n вершин."""
        self.n = n
        self.matrix = [[0] * n for _ in range(n)]

    def add_vertex(self, v=None):
        """Добавление вершины (индекс автоматически)."""
        self.n += 1
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * self.n)
        return self.n - 1  # возвращаем индекс новой вершины

    def remove_vertex(self, v):
        """Удаление вершины v."""
        self.matrix.pop(v)
        for row in self.matrix:
            row.pop(v)
        self.n -= 1

    def add_edge(self, u, v, weight=1):
        """Добавление ребра с весом."""
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight  # для неориентированного графа, убрать если ориентированный

    def remove_edge(self, u, v):
        """Удаление ребра."""
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0  # убрать если ориентированный

    def neighbors(self, v):
        """Список соседей с весами: [(vertex, weight), ...]"""
        return [(u, self.matrix[v][u]) for u in range(self.n) if self.matrix[v][u] != 0]

    def get_vertices(self):
        """Список всех вершин"""
        return list(range(self.n))

class AdjacencyList(Graph):
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def remove_vertex(self, v):
        if v in self.adj:
            self.adj.pop(v)
        for lst in self.adj.values():
            lst[:] = [(u, w) for u, w in lst if u != v]

    def add_edge(self, u, v, weight=1):
        self.add_vertex(u)
        self.add_vertex(v)
        if not any(x[0] == v for x in self.adj[u]):
            self.adj[u].append((v, weight))
        if not any(x[0] == u for x in self.adj[v]):  # для неориентированного графа
            self.adj[v].append((u, weight))

    def remove_edge(self, u, v):
        if u in self.adj:
            self.adj[u] = [(x, w) for x, w in self.adj[u] if x != v]
        if v in self.adj:
            self.adj[v] = [(x, w) for x, w in self.adj[v] if x != u]

    def neighbors(self, v):
        return self.adj.get(v, [])

    def get_vertices(self):
        return list(self.adj.keys())
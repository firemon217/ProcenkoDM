from collections import defaultdict

class AdjacencyMatrixGraph:
    def __init__(self, num_vertices):
        """
        Инициализация графа с num_vertices вершинами.
        Память: O(V^2)
        """
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight=1):
        """
        Добавление ребра (u -> v)
        Время: O(1)
        """
        self.matrix[u][v] = weight

    def remove_edge(self, u, v):
        """
        Удаление ребра (u -> v)
        Время: O(1)
        """
        self.matrix[u][v] = 0

    def add_vertex(self):
        """
        Добавление новой вершины
        Время: O(V^2) (надо расширить все строки)
        Память: увеличивается на O(V)
        """
        self.num_vertices += 1
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * self.num_vertices)

    def remove_vertex(self, v):
        """
        Удаление вершины v
        Время: O(V^2) (надо удалить строку и столбец)
        """
        self.matrix.pop(v)
        for row in self.matrix:
            row.pop(v)
        self.num_vertices -= 1

from collections import defaultdict

class AdjacencyMatrixGraph:
    def __init__(self, num_vertices):
        """
        Инициализация графа с num_vertices вершинами.
        Память: O(V^2)
        """
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight=1):
        """
        Добавление ребра (u -> v)
        Время: O(1)
        """
        self.matrix[u][v] = weight

    def remove_edge(self, u, v):
        """
        Удаление ребра (u -> v)
        Время: O(1)
        """
        self.matrix[u][v] = 0

    def add_vertex(self):
        """
        Добавление новой вершины
        Время: O(V^2) (надо расширить все строки)
        Память: увеличивается на O(V)
        """
        self.num_vertices += 1
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * self.num_vertices)

    def remove_vertex(self, v):
        """
        Удаление вершины v
        Время: O(V^2) (надо удалить строку и столбец)
        """
        self.matrix.pop(v)
        for row in self.matrix:
            row.pop(v)
        self.num_vertices -= 1

class AdjacencyListGraph:
    def __init__(self):
        """
        Словарь: ключ = вершина, значение = список соседей с весами
        Память: O(V + E)
        """
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight=1):
        """
        Добавление ребра (u -> v)
        Время: O(1)
        """
        self.graph[u].append((v, weight))

    def remove_edge(self, u, v):
        """
        Удаление ребра (u -> v)
        Время: O(deg(u))
        """
        self.graph[u] = [pair for pair in self.graph[u] if pair[0] != v]

    def add_vertex(self, v):
        """
        Добавление вершины
        Время: O(1)
        """
        self.graph[v] = []

    def remove_vertex(self, v):
        """
        Удаление вершины и всех входящих рёбер
        Время: O(V + E)
        """
        self.graph.pop(v, None)
        for u in self.graph:
            self.graph[u] = [pair for pair in self.graph[u] if pair[0] != v]

class AdjacencyMatrix:
    def __init__(self, n):
        """Создание матрицы смежности для n вершин.
        Сложность: O(V^2)
        """
        self.n = n
        self.matrix = [[0] * n for _ in range(n)]

    def add_edge(self, u, v):
        """Добавление ребра между u и v.
        Сложность: O(1)
        """
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1  # для неориентированного графа

    def remove_edge(self, u, v):
        """Удаление ребра между u и v.
        Сложность: O(1)
        """
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    def add_vertex(self):
        """Добавление вершины.
        Сложность: O(V) — добавить 1 элемент в каждую строку + новая строка
        """
        self.n += 1
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * self.n)

    def remove_vertex(self, v):
        """Удаление вершины v.
        Сложность: O(V^2) — удаление строки и одного столбца в каждой строке
        """
        self.matrix.pop(v)
        for row in self.matrix:
            row.pop(v)
        self.n -= 1

class AdjacencyList:
    def __init__(self):
        """Создание пустого списка смежности.
        Сложность: O(1)
        """
        self.adj = {}

    def add_vertex(self, v):
        """Добавление вершины v.
        Сложность: O(1)
        """
        if v not in self.adj:
            self.adj[v] = []

    def remove_vertex(self, v):
        """Удаление вершины v и всех связанных рёбер.
        Сложность: O(V + E) — пройти по всем спискам смежности
        """
        if v in self.adj:
            self.adj.pop(v)
        for lst in self.adj.values():
            if v in lst:
                lst.remove(v)

    def add_edge(self, u, v):
        """Добавление ребра между u и v.
        Сложность: O(1)–O(K) — поиск в списке длины K (степень вершины)
        """
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if u not in self.adj[v]:
            self.adj[v].append(u)

    def remove_edge(self, u, v):
        """Удаление ребра между u и v.
        Сложность: O(K) — нужно найти v в списке соседей u
        """
        if u in self.adj and v in self.adj[u]:
            self.adj[u].remove(v)
        if v in self.adj and u in self.adj[v]:
            self.adj[v].remove(u)
       

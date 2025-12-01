import unittest
from graph_representation import AdjacencyListGraph, AdjacencyMatrixGraph
from graph_traversal import bfs, dfs_recursive, dfs_iterative
from shortest_path import connected_components, topological_sort, dijkstra

class TestGraphRepresentation(unittest.TestCase):

    def setUp(self):
        # Список смежности
        self.g_list = AdjacencyListGraph()
        for v in range(3):
            self.g_list.add_vertex(v)
        self.g_list.add_edge(0, 1)
        self.g_list.add_edge(1, 2)

        # Матрица смежности
        self.g_matrix = AdjacencyMatrixGraph(3)
        self.g_matrix.add_edge(0,1)
        self.g_matrix.add_edge(1,2)

    def test_add_remove_vertex_list(self):
        g = AdjacencyListGraph()
        g.add_vertex(5)
        self.assertIn(5, g.graph)
        g.remove_vertex(5)
        self.assertNotIn(5, g.graph)

    def test_add_remove_edge_list(self):
        g = AdjacencyListGraph()
        g.add_vertex(0)
        g.add_vertex(1)
        g.add_edge(0,1)
        self.assertIn((1,1), g.graph[0])
        g.remove_edge(0,1)
        self.assertNotIn((1,1), g.graph[0])

    def test_add_remove_vertex_matrix(self):
        g = AdjacencyMatrixGraph(2)
        g.add_vertex()
        self.assertEqual(g.num_vertices, 3)
        g.remove_vertex(2)
        self.assertEqual(g.num_vertices, 2)

    def test_add_remove_edge_matrix(self):
        g = AdjacencyMatrixGraph(2)
        g.add_edge(0,1)
        self.assertEqual(g.matrix[0][1], 1)
        g.remove_edge(0,1)
        self.assertEqual(g.matrix[0][1], 0)


class TestGraphTraversal(unittest.TestCase):

    def setUp(self):
        self.g = AdjacencyListGraph()
        for v in range(4):
            self.g.add_vertex(v)
        edges = [(0,1),(0,2),(1,2),(2,3)]
        for u,v in edges:
            self.g.add_edge(u,v)

    def test_bfs(self):
        distances, parents = bfs(self.g, 0)
        expected_distances = {0:0, 1:1, 2:1, 3:2}
        self.assertEqual(distances, expected_distances)

    def test_dfs_recursive(self):
        visited = dfs_recursive(self.g, 0)
        self.assertEqual(visited, {0,1,2,3})

    def test_dfs_iterative(self):
        visited = dfs_iterative(self.g, 0)
        self.assertEqual(visited, {0,1,2,3})


class TestGraphAlgorithms(unittest.TestCase):

    def setUp(self):
        # Граф для тестов
        self.g = AdjacencyListGraph()
        for v in range(6):
            self.g.add_vertex(v)
        edges = [(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]
        for u,v in edges:
            self.g.add_edge(u,v)

        # Граф с компонентами связности
        self.g_cc = AdjacencyListGraph()
        for v in range(4):
            self.g_cc.add_vertex(v)
        self.g_cc.add_edge(0,1)
        self.g_cc.add_edge(2,3)

        # Граф для Дейкстры
        self.g_d = AdjacencyListGraph()
        for v in range(4):
            self.g_d.add_vertex(v)
        edges = [(0,1,1),(0,2,4),(1,2,2),(2,3,1)]
        for u,v,w in edges:
            self.g_d.add_edge(u,v,w)

    def test_topological_sort(self):
        order = topological_sort(self.g)
        # Проверяем, что все зависимости выполнены
        index = {v:i for i,v in enumerate(order)}
        for u,v in [(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]:
            self.assertLess(index[u], index[v])

    def test_connected_components(self):
        cc = connected_components(self.g_cc)
        expected = [{0,1},{2,3}]
        self.assertEqual(len(cc), 2)
        self.assertTrue(all(set(comp) in expected for comp in cc))

    def test_dijkstra(self):
        distances, parents = dijkstra(self.g_d, 0)
        expected_distances = {0:0, 1:1, 2:3, 3:4}
        self.assertEqual(distances, expected_distances)
        self.assertEqual(parents[3], 2)
        self.assertEqual(parents[2], 1)


if __name__ == "__main__":
    print("\n=== Запуск тестов графов ===\n")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(__import__(__name__))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    print("\n=== Тестирование завершено ===\n")

import time
import random
import matplotlib.pyplot as plt
import networkx as nx
from graph_representation import AdjacencyMatrixGraph, AdjacencyListGraph
from graph_traversal import bfs, dfs_iterative

def generate_random_graph(num_vertices, edge_prob=0.1, weighted=False):
    g_matrix = AdjacencyMatrixGraph(num_vertices)
    g_list = AdjacencyListGraph()
    for v in range(num_vertices):
        g_list.add_vertex(v)

    for u in range(num_vertices):
        for v in range(num_vertices):
            if u != v and random.random() < edge_prob:
                weight = random.randint(1, 10) if weighted else 1
                g_matrix.add_edge(u, v, weight)
                g_list.add_edge(u, v, weight)
    return g_matrix, g_list

def measure_operations():
    sizes = [100, 500, 1000, 5000]  # для примера, можно увеличить
    bfs_times_matrix, bfs_times_list = [], []
    dfs_times_matrix, dfs_times_list = [], []

    print("=== Замеры времени BFS и DFS ===")
    print(f"{'Vertices':>8} | {'BFS List':>10} | {'BFS Matrix':>10} | {'DFS List':>10} | {'DFS Matrix':>10}")
    print("-"*60)

    for n in sizes:
        g_matrix, g_list = generate_random_graph(n, edge_prob=0.05)
        start = 0

        # BFS на списке
        t0 = time.time()
        bfs(g_list, start)
        t1 = time.time()
        bfs_list_time = t1 - t0
        bfs_times_list.append(bfs_list_time)

        # BFS на матрице
        t0 = time.time()
        class Wrapper:
            def __init__(self, matrix):
                self.graph = {i: [(j, matrix[i][j]) for j in range(len(matrix[i])) if matrix[i][j] != 0] for i in range(len(matrix))}
        bfs(Wrapper(g_matrix.matrix), start)
        t1 = time.time()
        bfs_matrix_time = t1 - t0
        bfs_times_matrix.append(bfs_matrix_time)

        # DFS на списке
        t0 = time.time()
        dfs_iterative(g_list, start)
        t1 = time.time()
        dfs_list_time = t1 - t0
        dfs_times_list.append(dfs_list_time)

        # DFS на матрице
        t0 = time.time()
        dfs_iterative(Wrapper(g_matrix.matrix), start)
        t1 = time.time()
        dfs_matrix_time = t1 - t0
        dfs_times_matrix.append(dfs_matrix_time)

        # Вывод в консоль
        print(f"{n:>8} | {bfs_list_time:10.6f} | {bfs_matrix_time:10.6f} | {dfs_list_time:10.6f} | {dfs_matrix_time:10.6f}")

    # Визуализация графиков
    plt.figure(figsize=(10,5))
    plt.plot(sizes, bfs_times_list, label="BFS List")
    plt.plot(sizes, bfs_times_matrix, label="BFS Matrix")
    plt.plot(sizes, dfs_times_list, label="DFS List")
    plt.plot(sizes, dfs_times_matrix, label="DFS Matrix")
    plt.xlabel("Число вершин")
    plt.ylabel("Время выполнения (сек)")
    plt.title("Сравнение BFS и DFS на разных представлениях графа")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    measure_operations()

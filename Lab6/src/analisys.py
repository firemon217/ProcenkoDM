import random
import time
import matplotlib.pyplot as plt
from binary_search_tree import BinarySearchTree

def build_balanced_tree(size):
    bst = BinarySearchTree()
    values = list(range(size))
    random.shuffle(values)  # случайный порядок
    for v in values:
        bst.insert(v)
    return bst

def build_degenerate_tree(size):
    bst = BinarySearchTree()
    for v in range(size):  # отсортированный порядок
        bst.insert(v)
    return bst

def measure_search_time(bst, queries):
    start = time.perf_counter()
    for q in queries:
        bst.search(q)
    end = time.perf_counter()
    return end - start

def experiment():
    sizes = [100, 500, 1000, 5000]
    search_count = 1000

    balanced_times = []
    degenerate_times = []

    for size in sizes:
        # Сбалансированное дерево
        bst_balanced = build_balanced_tree(size)
        queries = [random.randint(0, size-1) for _ in range(search_count)]
        t_bal = measure_search_time(bst_balanced, queries)
        balanced_times.append(t_bal)

        # Вырожденное дерево
        bst_deg = build_degenerate_tree(size)
        queries = [random.randint(0, size-1) for _ in range(search_count)]
        t_deg = measure_search_time(bst_deg, queries)
        degenerate_times.append(t_deg)

        print(f"Size={size}: balanced={t_bal:.6f}s, degenerate={t_deg:.6f}s")

    return sizes, balanced_times, degenerate_times

# Построение графиков
def plot_times(sizes, balanced_times, degenerate_times):
    plt.plot(sizes, balanced_times, label="Balanced BST", marker='o')
    plt.plot(sizes, degenerate_times, label="Degenerate BST", marker='x')
    plt.xlabel("Number of elements")
    plt.ylabel("Time for 1000 searches (seconds)")
    plt.title("Search time in BST")
    plt.legend()
    plt.grid(True)
    plt.xscale('log')  # логарифмическая шкала по X
    plt.yscale('log')  # логарифмическая шкала по Y
    plt.show()

if __name__ == "__main__":
    # Эксперимент
    sizes, balanced_times, degenerate_times = experiment()

    # Визуализация дерева (пример для 10 элементов)
    print("\nExample Balanced BST with 10 elements:")
    bst_example = build_balanced_tree(10)

    # Построение графиков
    plot_times(sizes, balanced_times, degenerate_times)

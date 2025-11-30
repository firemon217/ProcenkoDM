from greedy_algorithms import fractional_knapsack, huffman_coding
from itertools import combinations
import heapq
import random
import string
import time
import matplotlib.pyplot as plt
import networkx as nx

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

frac_result = fractional_knapsack(values, weights, capacity)
print(f"Результат жадного алгоритма (fractional): {frac_result}")

def knapsack_01_brute_force(values, weights, capacity):
    n = len(values)
    max_value = 0
    for r in range(1, n+1):
        for combo in combinations(range(n), r):
            total_weight = sum(weights[i] for i in combo)
            total_value = sum(values[i] for i in combo)
            if total_weight <= capacity:
                max_value = max(max_value, total_value)
    return max_value

exact_result = knapsack_01_brute_force(values, weights, capacity)
print(f"Оптимальный результат 0-1 рюкзака: {exact_result}")

if frac_result > exact_result:
    print("Жадный алгоритм для дробного рюкзака может дать большее значение,")
    print("чем оптимальный для дискретного 0-1 рюкзака — пример неоптимальности.")

# Функция генерации случайных частот символов
def generate_frequencies(num_symbols: int) -> dict:
    symbols = random.sample(string.ascii_letters + string.digits, num_symbols)
    frequencies = {s: random.randint(1, 1000) for s in symbols}
    return frequencies

# Эксперимент: замер времени работы
sizes = [10, 50, 100, 500, 1000, 2000]  # количество символов
times = []

for size in sizes:
    freqs = generate_frequencies(size)
    start_time = time.time()
    huffman_coding(freqs)
    end_time = time.time()
    times.append(end_time - start_time)
    print(f"Размер входных данных: {size}, время: {end_time - start_time:.6f} сек")

# Визуализация зависимости времени работы
plt.plot(sizes, times, marker='o')
plt.xlabel("Количество символов")
plt.ylabel("Время работы алгоритма Хаффмана (сек)")
plt.title("Зависимость времени работы алгоритма Хаффмана от размера входных данных")
plt.grid(True)
plt.show()

# Визуализация дерева Хаффмана для одного примера

def build_huffman_tree(freqs):
    class HuffmanNode:
        def __init__(self, freq, symbol=None, left=None, right=None):
            self.freq = freq
            self.symbol = symbol
            self.left = left
            self.right = right
        def __lt__(self, other):
            return self.freq < other.freq

    heap = [HuffmanNode(f, s) for s, f in freqs.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(node1.freq + node2.freq, left=node1, right=node2)
        heapq.heappush(heap, merged)
    
    return heap[0]

def add_edges(G, node, parent=None):
    if node is None:
        return
    if parent:
        G.add_edge(parent, node.symbol if node.symbol else str(id(node)))
    add_edges(G, node.left, node.symbol if node.symbol else str(id(node)))
    add_edges(G, node.right, node.symbol if node.symbol else str(id(node)))

# Пример
freqs_example = generate_frequencies(10)
root = build_huffman_tree(freqs_example)
G = nx.DiGraph()
add_edges(G, root)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="lightblue", arrows=False)
plt.show()
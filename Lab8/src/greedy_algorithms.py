from typing import List, Tuple
import heapq

# Задача о выборе заявок (Interval Scheduling)
def interval_scheduling(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Выбирает максимальное количество непересекающихся интервалов.
    Жадный выбор: сортировка по времени окончания.
    """
    # Сортируем интервалы по времени окончания (раньше заканчиваются – приоритет)
    intervals.sort(key=lambda x: x[1])
    
    selected = []
    end_time = float('-inf')  # конец последнего выбранного интервала
    
    for interval in intervals:
        start, end = interval
        if start >= end_time:
            selected.append(interval)
            end_time = end  # обновляем время окончания последнего выбранного интервала
    
    return selected

# Временная сложность: O(n log n) из-за сортировки. Жадный выбор корректен, так как выбирая
# интервал с наименьшим окончанием, мы оставляем максимум места для будущих интервалов,
# что гарантирует оптимальное количество выбранных интервалов.

# Непрерывный рюкзак (Fractional Knapsack)
def fractional_knapsack(values: List[int], weights: List[int], capacity: int) -> float:
    """
    Максимизирует стоимость содержимого рюкзака, если можно брать дробные части предметов.
    Жадный выбор: сортировка по удельной стоимости.
    """
    items = sorted(
        [(v, w, v / w) for v, w in zip(values, weights)],
        key=lambda x: x[2],
        reverse=True
    )
    
    total_value = 0.0
    remaining_capacity = capacity
    
    for value, weight, ratio in items:
        if remaining_capacity >= weight:
            total_value += value
            remaining_capacity -= weight
        else:
            total_value += ratio * remaining_capacity
            break
    
    return total_value

# Временная сложность: O(n log n) из-за сортировки. Жадный выбор корректен, так как беря
# сначала предметы с наибольшей удельной стоимостью, мы максимально эффективно заполняем
# рюкзак, что гарантирует оптимальное решение для дробной задачи.

# Алгоритм Хаффмана (Huffman Coding)
class HuffmanNode:
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        
    def __lt__(self, other):
        return self.freq < other.freq  # для работы с heapq

def huffman_coding(frequencies: dict) -> dict:
    """
    Строит оптимальный префиксный код Хаффмана.
    Жадный выбор: объединяем два узла с наименьшей частотой на каждом шаге.
    """
    heap = [HuffmanNode(freq, symbol) for symbol, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(node1.freq + node2.freq, left=node1, right=node2)
        heapq.heappush(heap, merged)
    
    root = heap[0]
    codes = {}
    
    def generate_codes(node, prefix=""):
        if node.symbol is not None:
            codes[node.symbol] = prefix
            return
        generate_codes(node.left, prefix + "0")
        generate_codes(node.right, prefix + "1")
    
    generate_codes(root)
    return codes

# Временная сложность: O(n log n), где n – количество символов. Жадный выбор корректен,
# так как объединение наименее частотных узлов минимизирует суммарную длину кодов, что
# гарантирует оптимальность по длине сообщения.


def min_coins(amount: int, coins=[200, 100, 50, 20, 10, 5, 2, 1]) -> dict:
    """
    Возвращает словарь {монета: количество}, минимальное число монет для суммы amount.
    """
    change = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            change[coin] = count
    return change
# Временная сложность: O(n), где n – количество типов монет. Жадный выбор корректен для
# стандартных наборов монет, так как большие номиналы кратны меньшим, что гарантирует минимальное число монет.


def prim_mst(graph: dict) -> list:
    """
    graph: {node: [(neighbor, weight), ...], ...}
    Возвращает список рёбер MST в формате (u, v, weight)
    """
    start = list(graph.keys())[0]
    visited = set([start])
    edges = [(w, start, v) for v, w in graph[start]]
    heapq.heapify(edges)
    mst = []

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for to, w in graph[v]:
                if to not in visited:
                    heapq.heappush(edges, (w, v, to))
    return mst
# Временная сложность: O(E log V), где E – количество рёбер, V – количество вершин. Жадный выбор корректен, так как на каждом шаге выбирается минимальное ребро,
# что гарантирует минимальную общую стоимость остовного дерева (теорема о корректности алгоритма Прима).
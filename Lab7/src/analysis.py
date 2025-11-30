import time
import random
import matplotlib.pyplot as plt
from heap import MinHeap
from heapsort import heapsort_in_place
from typing import List

# ------------------------------
# Замеры времени построения кучи
# ------------------------------
def measure_heap_build_times(sizes):
    insert_times = []
    build_times = []

    for n in sizes:
        data = random.sample(range(n * 10), n)

        # Последовательная вставка
        heap = MinHeap()
        start = time.perf_counter()
        for x in data:
            heap.insert(x)
        t_insert = time.perf_counter() - start
        insert_times.append(t_insert)

        # Построение через build_heap
        heap2 = MinHeap()
        start = time.perf_counter()
        heap2.build_heap(data)
        t_build = time.perf_counter() - start
        build_times.append(t_build)

        print(f"[{n} элементов] Sequential insert: {t_insert:.6f}s, Build_heap: {t_build:.6f}s")

    return insert_times, build_times

# ------------------------------
# Замеры времени сортировки
# ------------------------------
def measure_sort_times(sizes):
    heapsort_times = []
    timsort_times = []
    quicksort_times = []

    for n in sizes:
        data = random.sample(range(n * 10), n)

        # Heapsort in-place
        arr = data[:]
        start = time.perf_counter()
        heapsort_in_place(arr)
        t_heap = time.perf_counter() - start
        heapsort_times.append(t_heap)

        # TimSort встроенный
        arr = data[:]
        start = time.perf_counter()
        sorted(arr)
        t_tim = time.perf_counter() - start
        timsort_times.append(t_tim)

        # QuickSort
        arr = data[:]
        start = time.perf_counter()
        quicksort(arr)
        t_qs = time.perf_counter() - start
        quicksort_times.append(t_qs)

        print(f"[{n} элементов] Heapsort: {t_heap:.6f}s, TimSort: {t_tim:.6f}s, QuickSort: {t_qs:.6f}s")

    return heapsort_times, timsort_times, quicksort_times

# ------------------------------
# Простейный QuickSort
# ------------------------------
def quicksort(arr: List[int]):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    arr[:] = quicksort(left) + mid + quicksort(right)
    return arr

# ------------------------------
# Текстовая визуализация MinHeap
# ------------------------------
def print_heap(heap_list, index=0, indent=0):
    if index >= len(heap_list):
        return
    right = 2 * index + 2
    left = 2 * index + 1
    print_heap(right, indent + 4)
    print(" " * indent + str(heap_list[index]))
    print_heap(left, indent + 4)

# ------------------------------
# Графическая визуализация MinHeap
# ------------------------------
def plot_heap_graph(heap_list):
    positions = {}

    def dfs(index, x, y, level=0):
        if index >= len(heap_list):
            return
        positions[index] = (x, y)
        left = 2*index + 1
        right = 2*index + 2
        offset = 1.0/(2**(level+1))
        dfs(left, x - offset, y - 1, level + 1)
        dfs(right, x + offset, y - 1, level + 1)

    dfs(0, 0.5, 0)

    plt.figure(figsize=(8,4))
    for i, (x, y) in positions.items():
        plt.scatter(x, -y, s=100)
        plt.text(x, -y, str(heap_list[i]), ha='center', va='center', color='white', fontsize=9)
        left = 2*i + 1
        right = 2*i + 2
        if left in positions:
            plt.plot([x, positions[left][0]], [-y, -positions[left][1]], 'k-')
        if right in positions:
            plt.plot([x, positions[right][0]], [-y, -positions[right][1]], 'k-')
    plt.axis('off')
    plt.show()

# ------------------------------
# Построение графиков
# ------------------------------
def plot_times(sizes, times_dict, title):
    plt.figure(figsize=(10,6))
    for label, times in times_dict.items():
        plt.plot(sizes, times, marker='o', label=label)
    plt.xlabel("Количество элементов")
    plt.ylabel("Время, сек")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# ------------------------------
# Главная функция
# ------------------------------
def main():
    sizes = [100, 500, 1000, 2000, 5000]

    print("\n=== Замеры времени построения кучи ===")
    insert_times, build_times = measure_heap_build_times(sizes)
    plot_times(sizes,
               {"Sequential insert": insert_times, "Build_heap": build_times},
               "Сравнение методов построения кучи")

    print("\n=== Замеры времени сортировки ===")
    heapsort_times, timsort_times, quicksort_times = measure_sort_times(sizes)
    plot_times(sizes,
               {"Heapsort": heapsort_times, "TimSort": timsort_times, "QuickSort": quicksort_times},
               "Сравнение Heapsort, TimSort и QuickSort")

if __name__ == "__main__":
    main()

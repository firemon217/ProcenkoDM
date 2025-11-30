from typing import List
from heap import MinHeap

def heapsort(array: List[int]) -> List[int]:
    """Heapsort через отдельную MinHeap"""
    heap = MinHeap()
    for x in array:
        heap.insert(x)
    sorted_array = [heap.extract() for _ in range(len(array))]
    return sorted_array

def heapsort_in_place(array: List[int]) -> List[int]:
    """Heapsort с использованием in-place алгоритма"""
    n = len(array)
    # Построение max-кучи (heapify)
    for start in range((n - 2) // 2, -1, -1):
        _sift_down(array, start, n - 1)
    
    # Извлечение элементов из кучи
    for end in range(n - 1, 0, -1):
        array[0], array[end] = array[end], array[0]  # перемещаем максимум в конец
        _sift_down(array, 0, end - 1)
    
    return array  # массив отсортирован по возрастанию

# --- Вспомогательные функции для in-place Heapsort ---
def _sift_down(arr: List[int], start: int, end: int):
    """Погружение элемента вниз для восстановления свойства кучи"""
    root = start
    while True:
        child = 2 * root + 1  # левый потомок
        if child > end:
            break
        if child + 1 <= end and arr[child + 1] > arr[child]:
            child += 1  # выбираем больший потомок
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break
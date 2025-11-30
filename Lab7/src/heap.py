from typing import List, Optional

class MinHeap:
    """Мин-куча на основе массива"""
    def __init__(self):
        self.heap: List[int] = []

    def _sift_up(self, index: int):
        """Всплытие элемента вверх для восстановления свойства кучи"""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2
    # Временная сложность: O(log n)

    def _sift_down(self, index: int):
        """Погружение элемента вниз для восстановления свойства кучи"""
        n = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
    # Временная сложность: O(log n)

    def insert(self, value: int):
        """Вставка элемента в кучу"""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
    # Временная сложность: O(log n)

    def extract(self) -> Optional[int]:
        """Извлечение корня (минимального элемента)"""
        if not self.heap:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return root
    # Временная сложность: O(log n)

    def peek(self) -> Optional[int]:
        """Просмотр корня без удаления"""
        return self.heap[0] if self.heap else None
    # Временная сложность: O(1)

    def build_heap(self, array: List[int]):
        """Построение кучи из произвольного массива"""
        self.heap = array[:]
        n = len(self.heap)
        # Запускаем _sift_down с последних родителей до корня
        for i in range((n - 2) // 2, -1, -1):
            self._sift_down(i)
    # Временная сложность: O(n)

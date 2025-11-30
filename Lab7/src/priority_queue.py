from heap import MinHeap
from typing import Any

class PriorityQueue:
    """Приоритетная очередь на основе MinHeap"""
    def __init__(self):
        self._heap = MinHeap()

    def enqueue(self, item: Any, priority: int):
        """Добавление элемента с приоритетом"""
        self._heap.insert((priority, item))
        # Время: O(log n)

    def dequeue(self) -> Any:
        """Извлечение элемента с наивысшим приоритетом (минимальный приоритет)"""
        element = self._heap.extract()
        return element[1] if element else None
        # Время: O(log n)

    def peek(self) -> Any:
        """Просмотр элемента с наивысшим приоритетом"""
        element = self._heap.peek()
        return element[1] if element else None
        # Время: O(1)
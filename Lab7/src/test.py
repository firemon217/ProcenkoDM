import unittest
from heap import MinHeap
from heapsort import heapsort, heapsort_in_place
from priority_queue import PriorityQueue

class TestHeap(unittest.TestCase):

    def setUp(self):
        self.values = [5, 3, 8, 1, 9, 2]

    def test_min_heap_insert_extract(self):
        heap = MinHeap()
        for v in self.values:
            heap.insert(v)
        # Проверяем, что после вставки свойство кучи сохраняется
        sorted_vals = []
        while heap.peek() is not None:
            sorted_vals.append(heap.extract())
        self.assertEqual(sorted_vals, sorted(self.values))

    def test_build_heap(self):
        heap = MinHeap()
        heap.build_heap(self.values)
        sorted_vals = []
        while heap.peek() is not None:
            sorted_vals.append(heap.extract())
        self.assertEqual(sorted_vals, sorted(self.values))

    def test_heapsort(self):
        sorted_array = heapsort(self.values)
        self.assertEqual(sorted_array, sorted(self.values))

    def test_heapsort_in_place(self):
        arr = self.values[:]
        sorted_arr = heapsort_in_place(arr)
        self.assertEqual(sorted_arr, sorted(self.values))

class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = PriorityQueue()
        self.items = [('task1', 5), ('task2', 1), ('task3', 3)]

    def test_enqueue_dequeue(self):
        for item, priority in self.items:
            self.pq.enqueue(item, priority)
        # Извлекаем элементы по приоритету (от минимального)
        extracted = [self.pq.dequeue() for _ in range(len(self.items))]
        expected_order = ['task2', 'task3', 'task1']
        self.assertEqual(extracted, expected_order)

    def test_peek(self):
        for item, priority in self.items:
            self.pq.enqueue(item, priority)
        self.assertEqual(self.pq.peek(), 'task2')  # минимальный приоритет = 1

if __name__ == "__main__":
    unittest.main(verbosity=2)
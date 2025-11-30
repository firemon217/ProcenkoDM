
from typing import Optional, Tuple, List

class HashTableChaining:
    def __init__(self, size: int = 8):
        # size корзин (bucket'ов)
        self.size = max(1, size)
        # Каждая корзина — список (цепочка)
        self.table: List[List[Tuple[object, object]]] = [[] for _ in range(self.size)]
        self.count = 0

    def _resize(self):
        """Рехеширование при превышении load factor."""
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        # Перемещаем всё в новую таблицу
        for bucket in old_table:
            for k, v in bucket:
                self.insert(k, v)

    def insert(self, key, value):
        """Вставка в цепочке."""
        index = hash(key) % self.size
        bucket = self.table[index]

        # Ищем ключ — если найден, обновляем
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Иначе добавляем в конец цепочки
        bucket.append((key, value))
        self.count += 1

        # При load_factor > 0.75 — удвоение таблицы
        if self.count / self.size > 0.75:
            self._resize()

    def search(self, key):
        """Поиск в цепочке."""
        index = hash(key) % self.size
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key) -> bool:
        """Удаление из цепочки."""
        index = hash(key) % self.size
        bucket = self.table[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.count -= 1
                return True

        return False
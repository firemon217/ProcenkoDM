from typing import Optional, Tuple, List

class HashTableLinear:
    def __init__(self, size: int = 8):
        # Минимальный размер таблицы — 2
        self.size = max(2, size)
        # Внутренний массив слотов
        # Каждый слот — либо None, либо (key, value), либо маркер deleted
        self.table: List[Optional[Tuple[object, object]]] = [None] * self.size
        # Уникальный объект, обозначающий удалённый элемент
        self.deleted = object()
        # Количество действительных записей (без учёта deleted)
        self.count = 0

    def _resize(self):
        """Увеличение размера таблицы в 2 раза с ре-хешированием."""
        old_table = self.table
        old_size = self.size

        # Увеличиваем размер
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0  # Пересчитаем при вставке

        # Вставляем старые элементы заново
        for slot in old_table:
            if isinstance(slot, tuple) and len(slot) == 2:
                self.insert(slot[0], slot[1])

    def insert(self, key, value):
        """Вставка элемента с линейным пробированием."""
        index = hash(key) % self.size
        first_deleted_index = None  # запомним первую встреченную "дыру"

        while True:
            slot = self.table[index]

            if slot is None:
                # Место пустое — вставляем
                if first_deleted_index is not None:
                    # Лучше заполнить ранее встреченную "дыру"
                    self.table[first_deleted_index] = (key, value)
                else:
                    self.table[index] = (key, value)
                self.count += 1
                break

            if slot is self.deleted:
                # Встретили удалённый слот — возможно, вставим сюда
                if first_deleted_index is None:
                    first_deleted_index = index
            else:
                # Валидный слот
                stored_key, _ = slot
                if stored_key == key:
                    # Ключ уже есть — заменяем значение
                    self.table[index] = (key, value)
                    return

            # Переходим к следующему индексу (линейный шаг = 1)
            index = (index + 1) % self.size

        # Проверка load factor (заполненности)
        if self.count / self.size > 0.7:
            self._resize()

    def search(self, key):
        """Поиск элемента с линейным пробированием."""
        index = hash(key) % self.size
        start = index  # чтобы не зациклиться

        while True:
            slot = self.table[index]

            if slot is None:
                # Пустой слот означает — ключ не встречался
                return None

            if slot is not self.deleted:
                stored_key, stored_value = slot
                if stored_key == key:
                    return stored_value

            # Линейный шаг
            index = (index + 1) % self.size

            if index == start:
                # полный круг — ключ не найден
                return None

    def delete(self, key) -> bool:
        """Удаление ключа. Возвращает True, если удалён."""
        index = hash(key) % self.size
        start = index

        while True:
            slot = self.table[index]

            if slot is None:
                # Пустой слот — значит ключа точно нет
                return False

            if slot is not self.deleted:
                stored_key, _ = slot
                if stored_key == key:
                    # Заменяем запись маркером deleted
                    self.table[index] = self.deleted
                    self.count -= 1
                    return True

            index = (index + 1) % self.size
            if index == start:
                return False

class HashTableDoubleHash:
    def __init__(self, size: int = 8):
        # Минимальный размер 3 (для h2 — шаг не должен быть 0)
        self.size = max(3, size)
        self.table: List[Optional[Tuple[object, object]]] = [None] * self.size
        self.deleted = object()
        self.count = 0

    def _h1(self, key) -> int:
        """Основная хеш-функция."""
        return hash(key) % self.size

    def _h2(self, key) -> int:
        """Вторичная хеш-функция — шаг пробирования.
        Должен быть всегда > 0.
        Дарит лучшую дисперсию, чем линейное пробирование."""
        return 1 + (hash(key) % (self.size - 1))

    def _resize(self):
        """Расширение таблицы с ре-хешированием."""
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0

        for slot in old_table:
            if isinstance(slot, tuple) and len(slot):
                self.insert(slot[0], slot[1])

    def insert(self, key, value):
        """Вставка с двойным хешированием."""
        index = self._h1(key)
        step = self._h2(key)
        first_deleted_index = None

        while True:
            slot = self.table[index]

            if slot is None:
                # Пустое место для вставки
                if first_deleted_index is not None:
                    self.table[first_deleted_index] = (key, value)
                else:
                    self.table[index] = (key, value)
                self.count += 1
                break

            if slot is self.deleted:
                if first_deleted_index is None:
                    first_deleted_index = index
            else:
                # Валидная запись
                stored_key, _ = slot
                if stored_key == key:
                    # Обновление
                    self.table[index] = (key, value)
                    return

            # Прыжок по шагу h2
            index = (index + step) % self.size

        if self.count / self.size > 0.7:
            self._resize()

    def search(self, key):
        """Поиск с двойным хешированием."""
        index = self._h1(key)
        step = self._h2(key)
        start = index

        while True:
            slot = self.table[index]
            if slot is None:
                return None

            if slot is not self.deleted:
                stored_key, stored_value = slot
                if stored_key == key:
                    return stored_value

            index = (index + step) % self.size
            if index == start:
                return None

    def delete(self, key) -> bool:
        """Удаление в таблице с двойным хешированием."""
        index = self._h1(key)
        step = self._h2(key)
        start = index

        while True:
            slot = self.table[index]
            if slot is None:
                return False

            if slot is not self.deleted:
                stored_key, _ = slot
                if stored_key == key:
                    self.table[index] = self.deleted
                    self.count -= 1
                    return True

            index = (index + step) % self.size
            if index == start:
                return False
class HashTableChaining:
    def __init__(self, size=8):
        # Инициализация хеш-таблицы с методом цепочек
        self.size = size  # Начальный размер таблицы
        self.table = [[] for _ in range(size)]  # Создаем массив пустых списков (бакетов)
        self.count = 0  # Счетчик количества элементов в таблице

    def _resize(self):
        # Метод для увеличения размера таблицы при высокой нагрузке
        old_table = self.table  # Сохраняем старую таблицу
        self.size *= 2  # Увеличиваем размер в 2 раза
        self.table = [[] for _ in range(self.size)]  # Создаем новую пустую таблицу
        self.count = 0  # Сбрасываем счетчик (будет пересчитан при вставке)

        # Перехеширование всех элементов из старой таблицы в новую
        for bucket in old_table:  # Проходим по каждому бакету старой таблицы
            for key, value in bucket:  # Проходим по всем парам ключ-значение в бакете
                self.insert(key, value)  # Вставляем элемент в новую таблицу

    def insert(self, key, value):
        # Вставка пары ключ-значение в таблицу
        index = hash(key) % self.size  # Вычисляем индекс бакета с помощью встроенной hash()
        bucket = self.table[index]  # Получаем ссылку на бакет (список)

        # Проверяем, существует ли уже такой ключ в бакете
        for i, (k, _) in enumerate(bucket):
            if k == key:
                # Если ключ найден, обновляем значение
                bucket[i] = (key, value)
                return

        # Если ключ не найден, добавляем новую пару в конец бакета
        bucket.append((key, value))
        self.count += 1  # Увеличиваем счетчик элементов

        # Проверяем коэффициент загрузки (load factor)
        if self.count / self.size > 0.75:
            self._resize()  # Если нагрузка > 75%, увеличиваем таблицу

    def search(self, key):
        # Поиск значения по ключу
        index = hash(key) % self.size  # Вычисляем индекс бакета
        # Линейный поиск ключа в бакете
        for k, v in self.table[index]:
            if k == key:
                return v  # Возвращаем значение, если ключ найден
        return None  # Возвращаем None, если ключ не найден

    def delete(self, key):
        # Удаление элемента по ключу
        index = hash(key) % self.size  # Вычисляем индекс бакета
        bucket = self.table[index]  # Получаем ссылку на бакет
        # Ищем ключ в бакете
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)  # Удаляем элемент по индексу
                return True  # Возвращаем True при успешном удалении
        return False  # Возвращаем False, если ключ не найден
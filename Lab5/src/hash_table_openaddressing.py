class HashTableLinear:
    def __init__(self, size=8):
        # Инициализация хеш-таблицы с линейным пробированием
        self.size = size  # Начальный размер таблицы
        self.table = [None] * size  # Создаем массив с None (пустые ячейки)
        self.deleted = object()  # Специальный маркер для удаленных элементов
        self.count = 0  # Счетчик количества элементов

    def _resize(self):
        # Увеличение размера таблицы при высокой нагрузке
        old_data = self.table  # Сохраняем старую таблицу
        self.size *= 2  # Удваиваем размер
        self.table = [None] * self.size  # Создаем новую пустую таблицу
        self.count = 0  # Сбрасываем счетчик

        # Перехеширование всех элементов (исключая удаленные)
        for item in old_data:
            if item and item is not self.deleted:
                self.insert(item[0], item[1])  # Вставляем ключ-значение

    def insert(self, key, value):
        # Вставка пары ключ-значение
        index = hash(key) % self.size  # Первичный хеш
        # Линейное пробирование: ищем пустую ячейку или ячейку с удаленным элементом
        while self.table[index] not in (None, self.deleted):
            # Если ключ уже существует, обновляем значение
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            # Переходим к следующей ячейке (циклически)
            index = (index + 1) % self.size

        # Нашли пустую ячейку, вставляем элемент
        self.table[index] = (key, value)
        self.count += 1

        # Проверяем коэффициент загрузки
        if self.count / self.size > 0.7:
            self._resize()  # Увеличиваем таблицу при нагрузке > 70%

    def search(self, key):
        # Поиск значения по ключу
        index = hash(key) % self.size  # Первичный хеш
        # Линейный поиск до первой пустой ячейки
        while self.table[index] is not None:
            # Пропускаем удаленные элементы, проверяем ключ
            if self.table[index] is not self.deleted and self.table[index][0] == key:
                return self.table[index][1]  # Возвращаем значение
            index = (index + 1) % self.size  # Следующая ячейка
        return None  # Ключ не найден

    def delete(self, key):
        # Удаление элемента по ключу
        index = hash(key) % self.size  # Первичный хеш
        while self.table[index] is not None:
            if self.table[index][0] == key:
                # Заменяем на специальный маркер (логическое удаление)
                self.table[index] = self.deleted
                return True  # Успешное удаление
            index = (index + 1) % self.size
        return False  # Ключ не найден


class HashTableDoubleHash:
    def __init__(self, size=8):
        # Инициализация хеш-таблицы с двойным хешированием
        self.size = size
        self.table = [None] * size
        self.deleted = object()  # Маркер удаленных элементов
        self.count = 0

    def _h2(self, key):
        # Вторая хеш-функция для вычисления шага пробирования
        # Возвращает число от 1 до size-1 (включительно)
        return 1 + (hash(key) % (self.size - 1))

    def _resize(self):
        # Увеличение размера таблицы
        old = self.table  # Сохраняем старые данные
        self.size *= 2  # Удваиваем размер
        self.table = [None] * self.size  # Новая таблица
        self.count = 0  # Сбрасываем счетчик

        # Перехеширование всех валидных элементов
        for entry in old:
            if entry and entry is not self.deleted:
                self.insert(*entry)  # Распаковываем кортеж (key, value)

    def insert(self, key, value):
        # Вставка с двойным хешированием
        index = hash(key) % self.size  # Первая хеш-функция
        step = self._h2(key)  # Вторая хеш-функция для шага

        # Двойное пробирование: используем step для перемещения
        while self.table[index] not in (None, self.deleted):
            if self.table[index][0] == key:
                # Обновление существующего ключа
                self.table[index] = (key, value)
                return
            # Переход с шагом step (циклически)
            index = (index + step) % self.size

        # Вставка в найденную ячейку
        self.table[index] = (key, value)
        self.count += 1

        # Проверка коэффициента загрузки
        if self.count / self.size > 0.7:
            self._resize()

    def search(self, key):
        # Поиск с двойным хешированием
        index = hash(key) % self.size  # Первый хеш
        step = self._h2(key)  # Шаг пробирования

        while self.table[index] is not None:
            # Проверяем ячейку (исключая удаленные)
            if self.table[index] is not self.deleted and self.table[index][0] == key:
                return self.table[index][1]
            # Переход с шагом step
            index = (index + step) % self.size
        return None

    def delete(self, key):
        # Удаление с двойным хешированием
        index = hash(key) % self.size
        step = self._h2(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                # Логическое удаление (маркер)
                self.table[index] = self.deleted
                return True
            index = (index + step) % self.size
        return False
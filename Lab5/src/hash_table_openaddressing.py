class HashTableLinear:
    def __init__(self, size=8):
        self.size = size
        self.table = [None] * size
        self.deleted = object()
        self.count = 0

    def _resize(self):
        old_data = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0

        for item in old_data:
            if item and item is not self.deleted:
                self.insert(item[0], item[1])

    def insert(self, key, value):
        index = hash(key) % self.size
        while self.table[index] not in (None, self.deleted):
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size

        self.table[index] = (key, value)
        self.count += 1

        if self.count / self.size > 0.7:
            self._resize()

    def search(self, key):
        index = hash(key) % self.size
        while self.table[index] is not None:
            if self.table[index] is not self.deleted and self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

    def delete(self, key):
        index = hash(key) % self.size
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = self.deleted
                return True
            index = (index + 1) % self.size
        return False

class HashTableDoubleHash:
    def __init__(self, size=8):
        self.size = size
        self.table = [None] * size
        self.deleted = object()
        self.count = 0

    def _h2(self, key):
        return 1 + (hash(key) % (self.size - 1))

    def _resize(self):
        old = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0

        for entry in old:
            if entry and entry is not self.deleted:
                self.insert(*entry)

    def insert(self, key, value):
        index = hash(key) % self.size
        step = self._h2(key)

        while self.table[index] not in (None, self.deleted):
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + step) % self.size

        self.table[index] = (key, value)
        self.count += 1

        if self.count / self.size > 0.7:
            self._resize()

    def search(self, key):
        index = hash(key) % self.size
        step = self._h2(key)

        while self.table[index] is not None:
            if self.table[index] is not self.deleted and self.table[index][0] == key:
                return self.table[index][1]
            index = (index + step) % self.size

        return None

    def delete(self, key):
        index = hash(key) % self.size
        step = self._h2(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = self.deleted
                return True
            index = (index + step) % self.size
        return False

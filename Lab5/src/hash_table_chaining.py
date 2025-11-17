class HashTableChaining:
    def __init__(self, size=8):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key, value):
        index = hash(key) % self.size
        bucket = self.table[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

        if self.count / self.size > 0.75:
            self._resize()

    def search(self, key):
        index = hash(key) % self.size
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = hash(key) % self.size
        bucket = self.table[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return True
        return False
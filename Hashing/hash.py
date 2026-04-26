class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        self.table[index].append(key)

    def search(self, key):
        index = self.hash(key)
        return key in self.table[index]

# ใช้งาน
ht = HashTable(7)
ht.insert(12)
ht.insert(19)
ht.insert(17)
ht.insert(20)

print(ht.search(17))  # True
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0
        
    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)
            self.count += 1
            

    def search(self, key):
        index = self.hash(key)
        if self.table[index]:
            return True, index
        else:
            return False, index

    def delete(self,key):
        index = self.hash(key)
        if key in self.table[index]:
            self.table[index].remove(key)
            self.count -= 1
    
    def get_loadfactor(self):
        return self.count / self.size
    
    def display(self):
        for i, v in enumerate(self.table):
            print(f"Index {i}: {v}")
            
ht = HashTable(5)

data = [10,20,30,40,50,11]

# insert
for x in data:
    ht.insert(x)
    
ht.delete(20)
# แสดงตาราง
ht.display()
print(ht.get_loadfactor())
print(ht.search(10))
print(ht.search(11)) 
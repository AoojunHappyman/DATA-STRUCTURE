class HashTable:
      
  def __init__(self,size):
    self.size = size
    self.table =[[]for _ in range(size)]
    
  def hash(self,key):
    return key % self.size
  
  def name_to_number(self,name):
    total = 0
    for i in name:
      total += ord(i)
    return total
  
  def insert(self,name):
      key  = self.name_to_number(name)
      index = self.hash(key)
      self.table[index].append(name)
      
  def display(self):
        for i,v in enumerate(self.table):
              print(i,v)
  
names = ["ICT", "DST", "LUV"]

ht1 = HashTable(5)
for n in names:
    ht1.insert(n)
ht1.display()

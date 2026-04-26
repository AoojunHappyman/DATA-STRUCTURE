class ArrayBasedSequence:
    def __init__(self, capacity=4):
        self.data = [None] * capacity
        self.size = 0

    # เพิ่มข้อมูลท้าย
    def add(self, value):
        self._ensure_capacity()
        self.data[self.size] = value
        self.size += 1

    # แทรกข้อมูลที่ตำแหน่ง index
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Invalid index")

        self._ensure_capacity()

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.size += 1

    # ลบข้อมูลที่ index
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.size -= 1
        self.data[self.size] = None

    # ดึงค่า
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")
        return self.data[index]

    # ขนาดข้อมูล
    def length(self):
        return self.size

    # ขยาย array อัตโนมัติ
    def _ensure_capacity(self):
        if self.size == len(self.data):
            new_capacity = len(self.data) * 2
            new_data = [None] * new_capacity

            for i in range(self.size):
                new_data[i] = self.data[i]

            self.data = new_data

    # แสดงข้อมูล
    def print(self):
        for i in range(self.size):
            print(self.data[i], end=" ")
        print()


# ======================
# ตัวอย่างการใช้งาน
# ======================
seq = ArrayBasedSequence(3)

seq.add(10)
seq.add(20)
seq.add(30)
seq.add(40)   # ขยาย array อัตโนมัติ

seq.print()   # 10 20 30 40

seq.insert(2, 99)
seq.print()   # 10 20 99 30 40

seq.remove(1)
seq.print()   # 10 99 30 40

print("Value at index 2:", seq.get(2))
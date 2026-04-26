# 📚 สรุป Array-Based Sequence (Python)

---

## 📌 แนวคิดหลัก

Array-Based Sequence คือโครงสร้างข้อมูลที่ใช้ **list (array)** ในการเก็บข้อมูลแบบลำดับ (sequence)
โดยมีการควบคุมขนาดจริงด้วยตัวแปร `size` และสามารถขยายขนาดอัตโนมัติได้เมื่อเต็ม

---

## 📌 โครงสร้างสำคัญ

* `data` → list สำหรับเก็บข้อมูล
* `size` → จำนวนข้อมูลที่ใช้งานจริง
* `capacity` → ขนาดของ array ที่รองรับได้

---

## 📌 ฟังก์ชันหลัก

### 1. add(value)

เพิ่มข้อมูลต่อท้าย array

```python
def add(self, value):
    self._ensure_capacity()
    self.data[self.size] = value
    self.size += 1
```

---

### 2. insert(index, value)

แทรกข้อมูลในตำแหน่งที่กำหนด และเลื่อนข้อมูลไปทางขวา

```python
def insert(self, index, value):
    if index < 0 or index > self.size:
        raise IndexError("Invalid index")

    self._ensure_capacity()

    for i in range(self.size, index, -1):
        self.data[i] = self.data[i - 1]

    self.data[index] = value
    self.size += 1
```

---

### 3. remove(index)

ลบข้อมูลที่ตำแหน่ง index และเลื่อนข้อมูลไปทางซ้าย

```python
def remove(self, index):
    if index < 0 or index >= self.size:
        raise IndexError("Invalid index")

    for i in range(index, self.size - 1):
        self.data[i] = self.data[i + 1]

    self.size -= 1
    self.data[self.size] = None
```

---

### 4. get(index)

ดึงค่าจากตำแหน่งที่ต้องการ

```python
def get(self, index):
    if index < 0 or index >= self.size:
        raise IndexError("Invalid index")
    return self.data[index]
```

---

### 5. _ensure_capacity()

ขยายขนาด array เมื่อเต็ม (เพิ่มเป็น 2 เท่า)

```python
def _ensure_capacity(self):
    if self.size == len(self.data):
        new_capacity = len(self.data) * 2
        new_data = [None] * new_capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
```

---

## 📌 ตัวอย่างการใช้งาน

```python
seq = ArrayBasedSequence(3)

seq.add(10)
seq.add(20)
seq.add(30)
seq.add(40)

seq.print()   # 10 20 30 40

seq.insert(2, 99)
seq.print()   # 10 20 99 30 40

seq.remove(1)
seq.print()   # 10 99 30 40

print(seq.get(2))
```

---

## 📌 สรุปสั้น ๆ

* ใช้ list แทน array
* มี size แยกจาก capacity
* รองรับ add / insert / remove / get
* ขยายขนาดอัตโนมัติเมื่อเต็ม

---

## 🎯 Big Idea

Array-Based Sequence เป็นพื้นฐานของโครงสร้างข้อมูลอื่น ๆ เช่น

* Stack
* Queue
* Dynamic Array (Vector)

---

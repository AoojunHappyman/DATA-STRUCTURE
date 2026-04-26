# 📚 Summary: Stack, Queue, Deque (Python)

---

## 🔹 1. Stack (LIFO)

### 📌 แนวคิด
- Last In First Out (LIFO)
- ข้อมูลที่เข้าหลัง → ออกก่อน

### 📌 การทำงานหลัก
- push() → เพิ่มข้อมูล
- pop() → ลบข้อมูล
- peek() → ดูค่าบนสุด

### 📌 ตัวอย่าง
```python
s.push(10)
s.push(20)
s.pop()   # 20
```

### 📌 การใช้งาน
- Undo/Redo
- Expression evaluation
- Function call (call stack)

---

## 🔹 2. Queue (FIFO)

### 📌 แนวคิด
- First In First Out (FIFO)
- เข้าก่อน → ออกก่อน

### 📌 การทำงานหลัก
- enqueue() → เพิ่มท้าย
- dequeue() → เอาหน้าออก
- front() → ดูค่าหน้า

### 📌 ตัวอย่าง
```python
q.enqueue(10)
q.enqueue(20)
q.dequeue()  # 10
```

### 📌 การใช้งาน
- ระบบคิว
- Scheduling
- BFS (Graph)

---

## 🔹 3. Deque (Double-Ended Queue)

### 📌 แนวคิด
- เพิ่ม/ลบ ได้ทั้งหน้าและท้าย

### 📌 การทำงานหลัก
- add_front()
- add_rear()
- remove_front()
- remove_rear()

### 📌 ตัวอย่าง
```python
d.add_front(10)
d.add_rear(20)
d.remove_front()  # 10
```

### 📌 การใช้งาน
- Sliding window
- Palindrome check
- Hybrid Queue/Stack

---

## ⚖️ เปรียบเทียบ

| โครงสร้าง | ลักษณะ | เพิ่ม | ลบ |
|----------|--------|------|-----|
| Stack    | LIFO   | ท้าย | ท้าย |
| Queue    | FIFO   | ท้าย | หน้า |
| Deque    | Flexible | หน้า/ท้าย | หน้า/ท้าย |

---

## 📌 หมายเหตุ (Performance)

- list.pop(0) และ list.insert(0, x) → O(n)
- แนะนำใช้ collections.deque → O(1)

```python
from collections import deque
```

---

## 🎯 Big Idea
- Stack = ย้อนกลับ
- Queue = ตามลำดับเวลา
- Deque = ยืดหยุ่น

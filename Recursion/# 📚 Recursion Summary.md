# 📚 Recursion Summary (Python)

## 🔁 1. ทฤษฎี Recursion

Recursion คือกระบวนการที่ฟังก์ชัน **เรียกตัวเองซ้ำ ๆ** เพื่อแก้ปัญหา โดยจะแบ่งปัญหาใหญ่ให้เล็กลงเรื่อย ๆ จนถึงจุดสิ้นสุด

### 🔑 องค์ประกอบสำคัญ

* **Base Case** → เงื่อนไขหยุดการทำงานของ recursion
* **Recursive Case** → การเรียกฟังก์ชันตัวเอง

### 💡 แนวคิดสำคัญ

* แก้ปัญหาใหญ่ → แยกเป็นปัญหาย่อย
* ต้องเล็กลงเรื่อย ๆ เพื่อไปถึง Base Case

---

## 🔁 2. Factorial

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

---

## 🔢 3. Fibonacci

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

## 📦 4. Sum of List

```python
def sum_list(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_list(arr[1:])
```

---

## 🔍 5. Binary Search (Recursive)

```python
def binary_search(arr, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)
```

---

## ⚠️ 6. Key Points

* ต้องมี Base Case เสมอ
* ถ้าไม่มี → infinite recursion (โปรแกรมค้าง)
* เหมาะกับปัญหา Divide & Conquer เช่น tree, search, sorting
* ใช้ memory มากกว่าการ loop ในบางกรณี

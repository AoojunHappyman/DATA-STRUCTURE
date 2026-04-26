# 🌳 COMPLETE TREE SUMMARY (สอบจบในไฟล์เดียว)

---

# 📌 1. Tree Basics

## 🔹 โครงสร้าง

* Root = โหนดบนสุด
* Parent / Child
* Leaf = ไม่มีลูก

---

# 📌 2. Traversal (สำคัญมาก)

## 🔥 จำให้ขึ้นใจ

```text
Preorder  = Root → Left → Right
Inorder   = Left → Root → Right
Postorder = Left → Right → Root
BFS       = Level by level
```

---

## 🔹 Preorder

```python
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)
```

---

## 🔹 Inorder ⭐

```python
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)
```

👉 BST จะได้ sorted

---

## 🔹 Postorder

```python
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)
```

---

## 🔹 BFS

```python
from collections import deque

def bfs(root):
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.data)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
```

---

# 📌 3. Binary Search Tree (BST)

## 🔥 กฎ

```text
Left < Root < Right
```

---

## 🔹 Insert

```python
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root
```

---

## 🔹 Search

```python
def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)
```

---

## 🔹 Delete

1. ไม่มีลูก → ลบทิ้ง
2. มีลูก 1 → เอาลูกแทน
3. มีลูก 2 → ใช้ inorder successor

---

## 🔥 BST + Inorder

```text
ได้ค่าจากน้อย → มาก
```

---

# 📌 4. Depth & Height

## 🔹 Depth

* ระยะจาก root → node

## 🔹 Height

* ระยะจาก node → leaf ที่ลึกสุด

---

## 🔹 Height (edge)

```python
def height(node):
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))
```

---

## 🔹 Height (node)

```python
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))
```

---

# 📌 5. Recursion Pattern

```python
def f(node):
    if node is None:
        return
    f(node.left)
    f(node.right)
```

---

# 📌 6. จุดหลอกในข้อสอบ (สำคัญสุด)

## ❗ 1. ตำแหน่ง print

* ก่อน = Preorder
* กลาง = Inorder
* หลัง = Postorder

---

## ❗ 2. print อยู่ใน loop

```python
for child:
    f(child)
    print(node)
```

👉 node จะถูก print หลายครั้ง

---

## ❗ 3. base case

```python
return -1  # นับ edge
return 0   # นับ node
```

---

## ❗ 4. +1 / +2

👉 ทำให้ height เปลี่ยน

---

## ❗ 5. recursion ไม่ครบ

```python
return f(left)
```

👉 อาจไม่ไปอีกฝั่ง

---

# 📌 7. ตัวอย่างโจทย์โหด

## 🔥 Weird Height

```python
def weird_height(node):
    if node is None:
        return -1
    left = weird_height(node.left)
    right = weird_height(node.right)
    if left > right:
        return left + 2
    else:
        return right + 1
```

👉 ต้องไล่จาก leaf ขึ้น root

---

## 🔥 Depth แบบเลือกทาง

```python
def depth_special(root, target, d=0):
    if root is None:
        return -1
    if root.data == target:
        return d
    if d % 2 == 0:
        return depth_special(root.left, target, d+1)
    else:
        return depth_special(root.right, target, d+1)
```

👉 ไม่ได้ค้นทั้ง tree

---

# 📌 8. ทริคจำสอบ

* Inorder = ซ้าย กลาง ขวา
* BST → เรียง
* Depth = จากบนลง
* Height = จากล่างขึ้น
* ดู print = รู้ traversal

---

# 🎯 สรุปสุดท้าย

* Tree = โครงสร้างลำดับชั้น
* Traversal = วิธีเดิน node
* BST = มีลำดับ
* Recursion = หัวใจของทุกอย่าง

---


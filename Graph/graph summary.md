# 📚 Graph Traversal Summary (BFS, DFS, Matrix, Concepts)

---

## 🔹 1. Graph Representation

### ✅ Adjacency List

เก็บว่า node เชื่อมกับใครบ้าง

```python
A: [B, C]
B: [A]
```

---

### ✅ Adjacency Matrix

ตาราง n × n

|   | A | B | C |
| - | - | - | - |
| A | 0 | 1 | 1 |
| B | 1 | 0 | 0 |
| C | 1 | 0 | 0 |

* Row = จุดเริ่ม
* Column = จุดปลาย
* 1 = มีเส้น, 0 = ไม่มี

👉 Column sum = **indegree**
👉 Row sum = **outdegree**

---

## 🔹 2. Breadth-First Search (BFS)

### 🧠 แนวคิด

* ไป “กว้างก่อน”
* ใช้ **Queue**

### 🔁 ขั้นตอน

1. เริ่มจาก start
2. enqueue
3. dequeue → visit
4. enqueue neighbor ที่ยังไม่ visited

### ⏱ Complexity

* O(n + m) 

---

## 🔹 3. Depth-First Search (DFS)

### 🧠 แนวคิด

* ไป “ลึกก่อน”
* ใช้ **Stack / Recursion**

### 🔁 ขั้นตอน

1. visit node
2. ไป neighbor ตัวแรก
3. ลึกจนสุด
4. ย้อน (backtrack)

### ⏱ Complexity

* O(n + m) 

---

## 🔥 BFS vs DFS

| หัวข้อ    | BFS           | DFS     |
| --------- | ------------- | ------- |
| วิธี      | กว้าง         | ลึก     |
| โครงสร้าง | Queue         | Stack   |
| เหมาะกับ  | shortest path | explore |
| ลำดับ     | เป็นชั้น      | ตามทาง  |

---

## 🔹 4. Connected Components

👉 กลุ่ม node ที่ “ไปถึงกันได้”

### วิธีหา

* ใช้ DFS/BFS
* ทำซ้ำทุก node

---

## 🔹 5. Topological Sort

👉 เรียงลำดับใน Directed Graph

### เงื่อนไข

* ต้องเป็น DAG (ไม่มี cycle)

### แนวคิด

* เริ่มจาก indegree = 0
* ลบออก → ทำซ้ำ

---

## 🔹 6. Types of Graph

### ✅ Unweighted Graph

* ไม่มี weight
* ใช้ BFS หา shortest path

---

## 🔹 7. Edge Types (DFS)

| ประเภท  | ความหมาย      |
| ------- | ------------- |
| Tree    | ใช้ค้นพบ      |
| Back    | ย้อน ancestor |
| Forward | ไปลูก         |
| Cross   | ข้ามกิ่ง      |

---

## 🔹 8. defaultdict

```python
from collections import defaultdict

graph = defaultdict(list)
graph['A'].append('B')
```

👉 key ไม่มี → สร้างให้เลย

---

## 🔹 9. Isolated Node

```python
isolated = [u for u in adj 
            if len(adj[u]) == 0 and u not in all_targets]
```

👉 ไม่มีเข้า + ไม่มีออก

---

## 🔹 10. List → Matrix

### แนวคิด

1. หา node ทั้งหมด
2. map → index
3. สร้าง matrix
4. ใส่ค่า 1 ตาม edge

---

## 🎯 สรุปสั้น

* BFS = กว้าง (Queue)
* DFS = ลึก (Stack)
* Matrix = ตาราง
* List = รายชื่อ
* Column sum = indegree
* Row sum = outdegree

---

## 💥 ประโยคทอง

> Graph = Node + Edge
> BFS = คิว
> DFS = ดำน้ำ
> Matrix = ตาราง 0/1

---

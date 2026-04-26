# 📚 Hash & Hash Table Summary

---

## 🔹 1. Hash คืออะไร

**Hash** คือการแปลงข้อมูล (**key**) ให้เป็นตัวเลข (**index**)
เพื่อใช้ระบุตำแหน่งใน Hash Table

```
key → hash function → index
```

---

## 🔹 2. Hash Function

ฟังก์ชันที่ใช้แปลง key → index

**ตัวอย่าง**

* Modulo: `h(k) = k % m`
* Mid-Square: เอาค่ากลางของ `k²`
* Folding: แบ่งเลขแล้วนำมาบวกกัน

---

## 🔹 3. Hash Table คืออะไร

โครงสร้างข้อมูลแบบ **array** ที่ใช้ hash function
เพื่อเก็บและค้นหาข้อมูลได้อย่างรวดเร็ว

---

## 🔹 4. การทำงานหลัก

### ➕ Insert

1. คำนวณ hash
2. นำไปเก็บที่ index

### 🔎 Search

1. คำนวณ hash
2. ไปดูตำแหน่งนั้น

### ❌ Delete

1. หา index
2. ลบข้อมูล

---

## 🔹 5. Collision คืออะไร

เกิดเมื่อ:

```
key ต่างกัน → index เดียวกัน
```

---

## 🔹 6. วิธีแก้ Collision

### 6.1 Separate Chaining

ใช้ list เก็บหลายค่าใน index เดียว

```
Index 5: [12, 19, 26]
```

### 6.2 Open Addressing

หาช่องใหม่แทน

* **Linear Probing**
  `(h(k) + i) % m`

* **Quadratic Probing**
  `(h(k) + i²) % m`

* **Double Hashing**
  `(h1(k) + i*h2(k)) % m`

---

## 🔹 7. Clustering

### 🔸 Primary Clustering

* เกิดใน Linear Probing
* ข้อมูลกระจุกติดกัน

### 🔸 Secondary Clustering

* เกิดใน Quadratic Probing
* key ที่ hash เท่ากัน → path ซ้ำ

---

## 🔹 8. Load Factor (α)

```
α = n / m
```

* `n` = จำนวนข้อมูล
* `m` = ขนาด table

| ค่า α  | ความหมาย |
| ------ | -------- |
| < 0.5  | โล่ง     |
| ~0.7   | ดี       |
| > 0.75 | เริ่มชน  |
| > 1    | ปัญหา    |

---

## 🔹 9. Rehashing

เมื่อ table แน่น:

* เพิ่มขนาด table
* คำนวณ hash ใหม่ทั้งหมด

---

## 🔹 10. Time Complexity

| Operation | Average | Worst |
| --------- | ------- | ----- |
| Insert    | O(1)    | O(n)  |
| Search    | O(1)    | O(n)  |
| Delete    | O(1)    | O(n)  |

---

## 🔹 11. เปรียบเทียบวิธี Hash

| วิธี       | ข้อดี        | ข้อเสีย    |
| ---------- | ------------ | ---------- |
| Modulo     | เร็ว         | ชนง่าย     |
| Folding    | กระจายดี     | คำนวณเพิ่ม |
| Mid-Square | ใช้ข้อมูลครบ | ซับซ้อน    |

---

## 🔹 12. สรุปสำคัญ (ออกสอบ)

* Hash = แปลง key → index
* Collision = index ซ้ำ
* Chaining = ใช้ list
* Open Addressing = หาช่องใหม่
* Load Factor = ความแน่น
* α สูง → ช้า

---

## 🔥 Trick จำง่าย

* **Hash** → หา index
* **Collision** → ชน
* **Chaining** → ซ้อน
* **Probing** → เลื่อน
* **α** → ความแน่น

---

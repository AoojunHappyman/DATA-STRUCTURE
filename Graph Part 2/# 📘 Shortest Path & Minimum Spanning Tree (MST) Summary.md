# 📘 Shortest Path & Minimum Spanning Tree (MST) Summary

---

# 🔷 1. Dijkstra’s Algorithm (Shortest Path)

## 📌 แนวคิด
- หาเส้นทางที่สั้นที่สุดจาก node เริ่มต้น → ทุก node
- ใช้กับ **weighted graph ที่ไม่มีค่าติดลบ**

---

## 📌 หลักการทำงาน
- เก็บระยะทางใน D[v]
- ใช้ Priority Queue เลือก node ที่ใกล้ที่สุดก่อน
- อัปเดตค่าด้วยเงื่อนไข:

> ถ้า D[v] > D[u] + w(u,v) → update

---

## 📌 ขั้นตอน
1. กำหนด D[start] = 0, ที่เหลือ = ∞
2. ใส่ node ลง Priority Queue
3. ทำซ้ำ:
   - เลือก node ที่ distance น้อยที่สุด
   - อัปเดตเพื่อนบ้าน

---

## 📌 ตัวอย่างผลลัพธ์
- D[BWI] = 0
- D[JFK] = 184
- D[ORD] = 621
- D[LAX] = 2658 :contentReference[oaicite:0]{index=0}  

---

## 📌 Time Complexity
- Heap → O((n + m) log n)
- Array → O(n²) :contentReference[oaicite:1]{index=1}  

---

# 🌳 2. Minimum Spanning Tree (MST)

## 📌 แนวคิด
- เชื่อมทุก node
- ไม่มี cycle
- น้ำหนักรวมน้อยที่สุด :contentReference[oaicite:2]{index=2}  

---

## 📌 Graph ที่ใช้
- Undirected
- Weighted :contentReference[oaicite:3]{index=3}  

---

## 📌 Definition
- Spanning Tree = เชื่อมทุก node
- MST = Spanning Tree ที่น้ำหนักน้อยที่สุด :contentReference[oaicite:4]{index=4}  

---

## 📌 แนวคิดสำคัญ
> ไม่ได้หา shortest path  
> แต่หา “โครงสร้างที่ถูกที่สุด” :contentReference[oaicite:5]{index=5}  

---

## 📌 ตัวอย่างปัญหา
- ต่อสาย network ให้ทุกเครื่องโดยใช้สายสั้นที่สุด :contentReference[oaicite:6]{index=6}  

---

# 🔥 3. Core Concept ของ MST

## ⭐ Greedy Algorithm
- เลือกสิ่งที่ดีที่สุดในแต่ละ step

---

## ⭐ Cut Property
- ถ้าแบ่ง graph เป็น 2 ฝั่ง  
- edge ที่เล็กที่สุดที่เชื่อมข้ามฝั่ง  
👉 ต้องอยู่ใน MST :contentReference[oaicite:7]{index=7}  

---

# ⚡ 4. Prim-Jarnik Algorithm

## 📌 แนวคิด
- เริ่มจาก node เดียว
- ค่อย ๆ ขยาย MST
- เลือก edge ที่เล็กที่สุดที่เชื่อมออกไป :contentReference[oaicite:8]{index=8}  

---

## 📌 วิธีทำ
1. เลือก node เริ่มต้น
2. ใช้ Priority Queue
3. เลือก edge ที่เล็กที่สุด
4. อัปเดต D[v] ถ้าเล็กกว่า

---

## 📌 ตัวอย่าง
- เริ่มจาก PVD
- เลือก JFK → BWI → BOS → ORD → ... :contentReference[oaicite:9]{index=9}  

---

## 📌 Time Complexity
- Heap → O((n + m) log n)
- Array → O(n²) :contentReference[oaicite:10]{index=10}  

---

# ⚡ 5. Kruskal’s Algorithm

## 📌 แนวคิด
- เริ่มจาก edge ที่เล็กที่สุด
- รวม cluster ทีละคู่
- ห้ามเกิด cycle :contentReference[oaicite:11]{index=11}  

---

## 📌 วิธีทำ
1. เรียง edge จากน้อย → มาก
2. เลือก edge:
   - ถ้าไม่เกิด cycle → เอา
   - ถ้าเกิด → ข้าม
3. หยุดเมื่อมี n-1 edges

---

## 📌 แนวคิด cluster
- เริ่มจาก n cluster
- รวม cluster ไปเรื่อย ๆ :contentReference[oaicite:12]{index=12}  

---

## 📌 ตัวอย่าง
- เพิ่ม (PVD, JFK)
- เพิ่ม (JFK, BWI)
- ถ้าเจอ edge ที่เชื่อมใน cluster เดิม → ไม่เลือก :contentReference[oaicite:13]{index=13}  

---

# 📊 6. เปรียบเทียบ Algorithm

| Algorithm | ใช้หา | เริ่มจาก | แนวคิด |
|----------|------|--------|-------|
| Dijkstra | Shortest Path | Node | Greedy |
| Prim | MST | Node | ขยาย |
| Kruskal | MST | Edge | รวม |

---

# ❗ 7. สิ่งที่ต้องระวัง

- MST ≠ Shortest Path
- Graph ต้อง connected
- MST อาจมีหลายคำตอบ
- จำนวน edge = n - 1

---

# 🎯 8. สรุปสั้น (เอาไปท่องสอบ)

- Dijkstra = หาเส้นทางสั้นสุด
- MST = เชื่อมครบ + ไม่วน + ถูกที่สุด
- Prim = ขยายจาก node
- Kruskal = เลือก edge
- ใช้ Greedy
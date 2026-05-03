def bubble_sort(arr):
    
    n = len(arr)
    # รอบการทำงาน (Pass) ทั้งหมดจะทำ n-1 รอบ
    for i in range(n):
        # สร้างตัวแปรเช็คว่ามีการสลับข้อมูลในรอบนี้หรือไม่ (เพื่อ Optimize)
        swapped = False
        # เปรียบเทียบข้อมูลคู่ที่อยู่ติดกัน
        # ทุกครั้งที่จบรอบ ตัวที่ค่ามากที่สุดจะไปอยู่ด้านขวาสุด จึงลดขอบเขตการเปรียบเทียบด้วย -i
        for j in range(0, n - i - 1):
            # หากตัวหน้า (Index j) มากกว่าตัวหลัง (Index j+1) ให้สลับที่กัน
            if arr[j] > arr[j + 1]:
                # การสลับค่า (Swap) ในภาษา Python
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # ถ้าจบรอบแล้วไม่มีการสลับข้อมูลเลย แสดงว่าข้อมูลเรียงลำดับเสร็จแล้ว
        if not swapped:
            break

# ตัวอย่างการใช้งาน
data = [45, 23, 87, 88, 32, 4]
print("Before:", data)

bubble_sort(data)

print("After:", data)
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # สมมติว่าตำแหน่ง i เป็นค่าที่น้อยที่สุด
        min_index = i
        
        # หา index ของค่าน้อยที่สุดในส่วนที่เหลือ
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # สลับค่า
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


# ตัวอย่างการใช้งาน
data = [64, 25, 12, 22, 11]
sorted_data = selection_sort(data)
print(sorted_data)
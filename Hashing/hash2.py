def name_to_number(name):
    # ขั้นตอนที่ 1: เปลี่ยนชื่อเป็นตัวเลขด้วยการรวมรหัส (ASCII)
    total = 0
    for i in name:
        total += ord(i)
    return total

def hash_function(key_number):
    # ขั้นตอนที่ 2: แฮชด้วยวิธีการหารเอาเศษ (ตารางขนาด 10 ช่อง)
    return key_number % 10

student = 'Somchai'
num_std = name_to_number(student)
idx = hash_function(num_std)

print(num_std)
print(idx)

def digit_folding_hash(key, r):
    key_str = str(key)   # แปลงเป็น string เพื่อแบ่งง่าย
    parts = []

    # แบ่งเป็นส่วนละ r หลัก
    for i in range(0, len(key_str), r):
        part = key_str[i:i+r]
        parts.append(int(part))

    # รวมค่าทุกส่วน
    total = sum(parts)

    # เอา r หลักท้าย
    hash_value = total % (10**r)

    return hash_value

x = 12345678
print(digit_folding_hash(x,2))

def mid_square_hash(key, r):
    square = key * key
    square_str = str(square)

    mid = len(square_str) // 2

    # หา index กลาง
    start = mid - (r // 2)
    end = start + r

    return int(square_str[start:end])

print(mid_square_hash(131, 2))
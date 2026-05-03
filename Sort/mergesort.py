def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # แบ่ง
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # รวม (merge)
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # เปรียบเทียบทีละตัว
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # เอาที่เหลือมาต่อ
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# 🔥 test
arr = [8, 3, 5, 2, 9, 1]
print("Merge Sort:", merge_sort(arr))
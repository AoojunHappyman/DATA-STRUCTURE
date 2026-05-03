def quick_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # เลือก pivot
    pivot = arr[0]

    # แบ่ง
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    # recursion
    return quick_sort(left) + [pivot] + quick_sort(right)


# 🔥 test
arr = [8, 3, 5, 2, 9, 1]
print("Quick Sort:", quick_sort(arr))
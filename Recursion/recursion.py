
# 1. Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# 2. Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# 3. Sum of List
def sum_list(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_list(arr[1:])


# 4. Binary Search (Recursive)
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


# Test
print(factorial(5))
print(fibonacci(6))
print(sum_list([1, 2, 3, 4]))
print(binary_search([1, 3, 5, 7, 9], 0, 4, 7))


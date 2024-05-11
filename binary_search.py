def binary_search(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


list_with_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12
index = binary_search(list_with_numbers, target)
print(index if index != -1 else f"Element {target} not found.")

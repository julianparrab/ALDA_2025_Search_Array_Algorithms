import math

### Linear Search ###
# Complexity:
# - Best Case: O(1)
# - Average Case: O(n)
# - Worst Case: O(n)

def linear_search(arr, target):
    for i in range(len(arr)):  # O(n)
        if arr[i] == target:  # O(1)
            return i  # O(1)
    return -1  # O(1)

### Binary Search ###
# Complexity:
#   - Best Case: O(1)
#   - Average Case: O(log n)
#   - Worst Case: O(log n)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:  # O(log n)
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # O(1)
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # O(1)


### Ternary Search ###
# Complexity:
#   - Best Case: O(1)
#   - Average Case: O(log_3 n)
#   - Worst Case: O(log_3 n)

def ternary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:  # O(log_3 n)
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if arr[mid1] == target:
            return mid1  # O(1)
        if arr[mid2] == target:
            return mid2  # O(1)
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left, right = mid1 + 1, mid2 - 1
    return -1  # O(1)

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    return -1

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
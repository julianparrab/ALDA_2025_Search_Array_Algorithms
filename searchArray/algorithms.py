import math
import numpy as np

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
    left, right = 0, len(arr) - 1  # O(1)
    while left <= right:  # O(log n)
        mid = (left + right) // 2  # O(1)
        if arr[mid] == target:  # O(1)
            return mid  # O(1)
        elif arr[mid] < target:  # O(1)
            left = mid + 1  # O(1)
        else:
            right = mid - 1  # O(1)
    return -1  # O(1)


### Ternary Search ###
# Complexity:
#   - Best Case: O(1)
#   - Average Case: O(log_3 n)
#   - Worst Case: O(log_3 n)


def ternary_search(arr, target):
    left = 0  # O(1)
    right = len(arr) - 1  # O(1)
    while left <= right:  # O(log_3 n)
        mid1 = left + (right - left) // 3  # O(1)
        mid2 = right - (right - left) // 3  # O(1)
        if arr[mid1] == target:
            return mid1  # O(1)
        if arr[mid2] == target:
            return mid2  # O(1)
        if target < arr[mid1]:
            right = mid1 - 1  # O(1)
        elif target > arr[mid2]:
            left = mid2 + 1  # O(1)
        else:
            left, right = mid1 + 1, mid2 - 1  # O(1)
    return -1  # O(1)


### Jump Search ###
# Complexity:
#   - Best Case: O(1)
#   - Average Case: O(sqrt(n))
#   - Worst Case: O(sqrt(n))


def jump_search(arr, target):
    n = len(arr)  # O(1)
    step = int(math.sqrt(n))  # O(1)
    prev = 0  # O(1)
    while arr[min(step, n) - 1] < target:  # O(sqrt(n))
        prev = step  # O(1)
        step += int(math.sqrt(n))  # O(1)
        if prev >= n:  # O(1)
            return -1
    while arr[prev] < target:  # O(sqrt(n))
        prev += 1
        if prev == min(step, n):  # O(1)
            return -1
    if arr[prev] == target:  # O(1)
        return prev
    return -1


### Interpolation Search ###
# user for uniformly distributed arrays
# Complexity:
#   - Best Case: O(1)
#   - Average Case: O(log log n)
#   - Worst Case: O(n)


def interpolation_search(arr, target):
    low = 0  # O(1)
    high = len(arr) - 1  # O(1)
    while low <= high and target >= arr[low] and target <= arr[high]:  # O(log log n)
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])  # O(1)
        if arr[pos] == target:  # O(1)
            return pos  # O(1)
        elif arr[pos] < target:  # O(1)
            low = pos + 1  # O(1)
        else:
            high = pos - 1  # O(1)
    return -1  # O(1)

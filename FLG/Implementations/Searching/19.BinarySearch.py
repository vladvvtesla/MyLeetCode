"""
The implementation here is an iterative one.
"""

def binary_search(arr, target):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
        if lo > hi:
            return None

if __name__ == '__main__':
    arr1 = [10,30,100,120,200]
    arr2 = [10, 30, 100, 120, 200, 400]
    print(binary_search(arr1, 30))
    print(binary_search(arr2, 400))
    print(binary_search(arr2, 500))
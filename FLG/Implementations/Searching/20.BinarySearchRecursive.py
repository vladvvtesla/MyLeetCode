"""
The implementation here is an recursive one.
"""

def bin_search(arr, lo, hi,target):
    if (hi < lo):
        return None
    else:
        mid = lo + ((hi - lo) // 2)
        if arr[mid] > target:
            return bin_search(arr, lo, mid-1,target)
        elif arr[mid] < target:
            return bin_search(arr, mid+1, hi, target)
        else:
            return mid

if __name__ == '__main__':
    arr1 = [10,30,100,120,200]
    arr2 = [10, 30, 100, 120, 200, 400]
    print(bin_search(arr1, 0, 5,30))
    print(bin_search(arr2, 0, 5, 400))
    print(bin_search(arr2, 0, 5, 500))
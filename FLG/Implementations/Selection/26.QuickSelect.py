"""
Quick Select

Search for the kth-smallest item

The worst-case performance of a randomized selection algorithm is O(n^2 )
"""

def partition(arr, lo, hi):
    if lo == hi:
        return lo

    pivot = arr[lo]
    pivot_idx = lo
    hi_idx = hi

    lt_pivot_idx = hi_idx
    gt_pivot_idx = lo + 1

    while True:
        while arr[gt_pivot_idx] < pivot and gt_pivot_idx < hi:
            gt_pivot_idx += 1
        while arr[lt_pivot_idx] > pivot and lt_pivot_idx >= lo:
            lt_pivot_idx -= 1

        if gt_pivot_idx < lt_pivot_idx:
            arr[gt_pivot_idx],arr[lt_pivot_idx] = arr[lt_pivot_idx],arr[gt_pivot_idx]
        else:
            break

    arr[pivot_idx] = arr[lt_pivot_idx]
    arr[lt_pivot_idx] = pivot
    return lt_pivot_idx


def quick_select(arr, left, right, k):
    """
    Search for the kth-smallest item
    :return:
    """
    split = partition(arr, left, right)
    if split == k:
        return arr[split]
    elif split < k:
        return quick_select(arr, split + 1, right, k)
    else:
        return quick_select(arr, left, split-1, k)

def test_quick_select():
    inp = [([2,3,1,6,4,5,7],0,6,6),
           ([200,300,100], 0, 2, 2),
           ]
    out = [7,300]

    for i in range(len(inp)):
        test_res = quick_select(inp[i][0],inp[i][1],inp[i][2],inp[i][3])
        print('test_res:', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_quick_select()



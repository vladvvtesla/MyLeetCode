"""
3-way quicksort: Python implementation

Duplicate keys
Mergesort with duplicate keys. Always between  1/2 NlgN and NlgN compares

Quicksort with duplicate keys. The classic algorithm goes quadratic unless partitioning stops on equal keys
Recommended: Stop scan on items equal to the partitioning item
Consequence: ~NlgN compares when all keys equal

Bottom line: Randomized quicksort with 3-way partitioning reduces running time from linearithmic to linear in a broad class of applications.
Quicksort with 3-way partitioning is most effective when the input array has a few distinct items?

Dijkstra 3-way partitioning

Engineering a system sort
Basic algorithm - quick sort
 - Cutoff to insertion sort for small subarrays
 - Partitioning scheme: 3-way partitioning
 - Partitioning items
      Large arrays: middle entry
      medium arrays: median of 3
      large arrays: Tukey's ninther
"""

def quicksort(a, lo, hi):
    """
    3-way quicksort: Python implementation
    :param a:  Array
    :param lo: low Index
    :param hi: high index
    """
    if hi <= lo:
        return
    lt, gt = lo, hi
    i = lo
    while i <= gt:
        if a[i] < a[lt]:
            a[lt],a[i] = a[i],a[lt]
            lt += 1
            i += 1
        elif a[i] > a[lo]:
            a[gt],a[i] = a[i],a[gt]
            gt -= 1
        else:
            i += 1

    quicksort(a, lo, lt - 1)
    quicksort(a, gt + 1, hi)

    # assert isSorted(a)            # Postcondition: a is sorted


def isSorted(a, asc=True):
    """
    Check if an array is sorted
    :param a: array
    :param asc: ascending or descending
    :return: boolean
    """
    s = 2*int(asc) - 1      # sign:   int(True)=1 => 2*1-1 = 1

    for i in range(len(a)-1):
        if s * a[i] > s * a[i+1]:
            return False
    return True


def test_quicksort():
    import random

    a = [6,2,9,2,5]
    a_sorted = [2,2,5,6,9]
    random.shuffle(a)             # Shuffle array only onсe
    quicksort(a, 0, len(a)-1)
    print("Test", "1.", "OK" if a == a_sorted else "Failed")
    print()

    b = [1,0,0,0,0]
    b_sorted = [0,0,0,0,1]
    random.shuffle(b)             # Shuffle array only onсу
    quicksort(b, 0, len(b)-1)
    print("Test", "2.", "OK" if b == b_sorted else "Failed")
    print()

    c = [1]
    c_sorted = [1]
    random.shuffle(c)
    quicksort(c, 0, len(c)-1)
    print("Test", "3.", "OK" if c == c_sorted else "Failed")
    print()


def test_isSorted():
    inp = [[0, 1, 2 , 3, 4], [6, 2, 9, 2, 5]]
    out = [True, False]
    for i in range(len(inp)):
        test_res = isSorted(inp[i])
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()


if __name__ == '__main__':
    print('test_quicksort')
    test_quicksort()

    print('test_isSorted')
    test_isSorted()

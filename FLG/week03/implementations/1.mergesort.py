"""


Mergesort Time Complexity:
Mergesort uses at most N * lg N  compares and at most 6 * N * lg N
array accesses to sort any array of size N

Mergesort Space Complexity:
Mergesort uses extra space proportional to N

Mergesort has too much overhead for tiny subarrays

Stop if already sorted:
Is the biggest item in the first half is smaller than the smallest item in the second hulf
Helps for partially ordered array

"""



def mergesort(a):
    """ Merging Sort implementation"""
    if len(a) <= 1:
        return                                     # сортируем на месте,поэтому просто возвращаем None
    middle = len(a) // 2
    l = [a[i] for i in range(0, middle)]           # Left half of the list
    r = [a[i] for i in range(middle, len(a))]      # Right half of the list
    mergesort(l)
    mergesort(r)
    c = merge(l, r)          # слияние двух списков
    for i in range(len(a)):  # новый отсортированный список скопировать в изначальный
        a[i] = c[i]


def merge(a: list, b: list):
    """
    Merging of two sorted arrays
    :param a:   firts sorted array
    :param b:   second sorted array
    :return c:  sorted array after merging
    """
    assert isSorted(a)                  # Precondition: is sorted
    assert isSorted(b)                  # Precondition: is sorted

    if a[-1] <= b[0]: c = a + b         # Stop if already sorted:

    c = [0] * (len(a) + len(b))
    i = k = n = 0                       # indexes for arrays a, b, c
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    while i < len(a):             # insert tail of a into c, if it exists
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]               # insert tail of b into c, if it exists
        k += 1
        n += 1

    assert isSorted(c)            # Postcondition: c is sorted

    return c


def isSorted(a):
    """
    Check if an array is sorted
    :param a: array
    :return: boolean
    """
    for i in range(len(a)-1):
        if a[i+1] < a[i]:
            return False
    return True


def test_mergesort():
    a = [6,2,9,2,5]
    a_sorted = [2,2,5,6,9]
    mergesort(a)
    print("Test", "1.", "OK" if a == a_sorted else "Failed")
    print()

    b = [1,0,0,0,0]
    b_sorted = [0,0,0,0,1]
    mergesort(b)
    print("Test", "2.", "OK" if b == b_sorted else "Failed")
    print()


def test_isSorted():
    inp = [[0, 1, 2 , 3, 4], [6, 2, 9, 2, 5]]
    out = [True, False]
    for i in range(len(inp)):
        test_res = isSorted(inp[i])
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()


if __name__ == '__main__':
    print('test_mergesort')
    test_mergesort()

    print('test_isSorted')
    test_isSorted()

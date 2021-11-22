"""

Merge Sort

"""


def merge(a, b):
    i = j = 0
    c = []

    if a[-1] <= b[0]: return a + b      # Stop if already sorted:

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1

    return c


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2

    l = a[:mid]
    r = a[mid:]

    half_a = merge_sort(l)
    half_b = merge_sort(r)

    return merge(half_a, half_b)


def test_merge_sort():
    inp = [[4, 2, 5, 2, 1], [4, 2, 5, 2, 1, 6], [0]]
    out = [[1, 2, 2, 4, 5], [1, 2, 2, 4, 5, 6], [0]]
    for i in range(len(inp)):
        test_res = merge_sort(inp[i])
        print('test_res:', test_res)
        print("Test " + str(i+1) + ": ", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_merge_sort()
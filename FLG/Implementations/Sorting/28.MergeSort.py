"""

Merge Sort

"""


def merge(a, b):
    i = j = 0
    c = []

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
    if len(a) == 1:
        return a
    mid = int((len(a))/2)

    l = a[:mid]
    r = a[mid:]

    half_a = merge_sort(l)
    half_b = merge_sort(r)

    return merge(half_a, half_b)


def test_merge_sort():
    a = [4, 2, 5, 2, 1]
    a_sorted = [1, 2, 2, 4, 5]
    test_res = merge_sort(a)
    print('test_res:', test_res)
    print("OK" if test_res == a_sorted else "Failed")


if __name__ == '__main__':
    test_merge_sort()
"""

1. Selection sort uses N^2/2 compareses
and N exchanges
2. Quadratic time , even if input is sorted

Time Complexity O ( N^2 )
"""
def select_sort(a):
    """ Selection Sort implementation"""
    n = len(a)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if a[j] <= a[min_i]:
                min_i = j
        a[i],a[min_i] = a[min_i],a[i]


def test_select_sort():
    a = [6,2,9,2,5]
    a_sorted = [2,2,5,6,9]
    select_sort(a)
    print("1.", "OK" if a == a_sorted else "Failed")

    b = [1,0,0,0,0]
    b_sorted = [0,0,0,0,1]
    select_sort(b)
    print("2.", "OK" if b == b_sorted else "Failed")


if __name__ == '__main__':
    test_select_sort()

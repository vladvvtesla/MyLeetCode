"""
1. To sort randomly-ordered array with distinct key,
Insertion sort uses ~ 1/4 * N^2 compareses
and ~ 1/4 * N^2  exchanges on average
2. Best Case. If the array is in ascending order,
Insertion sort makes N-1 compareses and 0 exchanges
3. Worst Case. If the array is in descending order,
Insertion sort makes ~ 1/2 * N^2 compareses and ~ 1/2 * N^2 exchanges
4. For partially-sorted arrays

Time Complexity O ( N^2 ) Insertion sort runs in linear time
"""
def insert_sort(a):
    """ Insertion Sort implementation"""
    n = len(a)
    for i in range(n):
        for j in range(i, 0, -1):
            if a[j] <= a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
            else:
                break


def test_insert_sort():
    a = [6,2,9,2,5]
    a_sorted = [2,2,5,6,9]
    insert_sort(a)
    print("1.", "OK" if a == a_sorted else "Failed")

    b = [1,0,0,0,0]
    b_sorted = [0,0,0,0,1]
    insert_sort(b)
    print("2.", "OK" if b == b_sorted else "Failed")


if __name__ == '__main__':
    test_insert_sort()

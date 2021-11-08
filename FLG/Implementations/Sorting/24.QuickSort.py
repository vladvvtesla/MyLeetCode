"""

"""

def quick_sort(a):
    """Сортировка списка А выбором"""

    def partition(unsorted_array, first_index, last_index):
        pivot = unsorted_array[first_index]
        pivot_index = first_index
        index_of_last_element = last_index

        less_than_pivot_index = index_of_last_element
        greater_than_pivot_index = first_index + 1

        while True:
            while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
                greater_than_pivot_index += 1
            while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
                less_than_pivot_index -= 1


    n = len(a)
    for pos in range(0, n-1):
        for k in range(pos+1, n):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]




def test_sort(sort_algorithm):
    print('Тестируем: ', sort_algorithm.__doc__)
    print('testcase #2: ', end='')
    a = list(range(10, 20)) + list(range(0, 10))
    a_sorted = list(range(20))
    sort_algorithm(a)
    print("OK" if a == a_sorted else "Failed")


if __name__ == '__main__':
    test_sort(quick_sort)

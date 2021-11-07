"""
Сортировка вставкой (insert sort)

 0-й элемент считатем отсортированным подмассивом
 Берем 1-й элемент и сравниваем его с 0-м
    Если 1-й < 0-го, то меняем эти элементы местами
    Иначе 1-й элемент оставляем в своем 1-ом  слоте
 Берем 2-й элемент и сравниваем его с 1-м,
     Если 2-й < 1-го, то меняем элементы местами,
     Затем сравниваем 1-й элемент с 0-м
          Если 1-й < 0-го, то меняем местами
          если достигли 0-слота, то прекращаем сравнения, чтобы не обратиться к -1 элементу
 точно также поступаем со 3-м, 4-м и остальными элементами массива

The insertion sort algorithm is considered stable in that it does not change the relative order
of elements that have equal keys. It also only requires no more memory than what is
consumed by the list because it does the swapping in-place.
Its worst case value is O(n 2 ) and its best case is O(n).
"""

A = [4,2,5,1,3]

def insert_sort(a):
    """Сортировка списка А вставками"""
    n = len(a)
    for top in range(1, n):
        k = top
        while k > 0 and a[k-1] > a[k]:
            a[k], a[k-1] = a[k-1], a[k]
            k -= 1

def test_sort(sort_algorithm):
    print('Тестируем: ', sort_algorithm.__doc__)
    print('testcase #1: ', end='')
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)
    print("OK" if a == a_sorted else "Failed")


if __name__ == '__main__':
    test_sort(insert_sort)
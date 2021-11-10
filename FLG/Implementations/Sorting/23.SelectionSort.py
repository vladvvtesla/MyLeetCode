"""

# 6.2.Сортировка выбором (selection (choise) sort)
#
#  идти по массиву в поисках минимального значения, пусть это будет i-й элемент
#  поменять местами 0-й и i-й элементы
#  Но мы еще не прошлись по всему массиву. Поэтому продолжить идти по массиву
#  в поисках минимального значения, пусть это будет j-й элемент
#  поменять местами 0-й и j-й элементы
#  Так пройтись по всему массиву.
#  Так только прошлись по всему массиву, то в 0-м слоте у нас самое минимальное значение
#  Точно также пройтись по подмассиву от 1-го до N-го элемента,
#  и на 1-й слот попадет второй по величине элемент
#  Теперь в 0-м и 1-м  слотах стоят отсортированные элементы на своих окончательных позициях
#  И алгоритм в эти слоты больше не заглядывает
#  Затем о подмассиву от 2-го до N-го элемента и так далее
#  Оказывается, что последнего сортировать не надо, он автоматически встает на свое окончательное место

The worst and the best asymptotic values is O(n^2 ).
"""

def choise_sort(a):
    """Сортировка списка А выбором"""
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
    test_sort(choise_sort)
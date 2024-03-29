
#  6.3.сортировка методом пузырька (bubble sort)
#
#  Сравнить 0-й и 1-й элементы,
#  и если они стоят в неправильном порядке, поменять местами
#  Сравнить 1-й и 2-й элементы,
#  и если они стоят в неправильном порядке, поменять местами,
#  если в правильном, оставить на своих местах
#  После первого такого прохода, в последнем N-м слоте окажется самый большой элемент.
#  Если где-то в середине наткнулись на самый большой элемент, то все дальнейшие сравнения
#  будут переставлять его на один элемент ближе к концу. То есть он всплывает как пузырек в воде
#  Затем снова пройти по всему массиву. Сравнить 0-й и 1-й элементы, и т. д.
#  Так как в конце у нас формируется отсортированный подмассив, то туда заглядывать уже не нужно
#  Для сортироваки 5 элементов, нужно 4 прохода
#  На первом проходе потребовалось 4 сравнения, на втором - 3 , на третьем, 2, на четвертом 1
#  то есть у нас количество проходов по массиву N-1, а количество сравнений в проходах
#  4+3+2+1 - это арифметическая прогрессия.
#  Сумма N -первых членов арифметической прогрессии пропорциональна 1/2 * N * (N-1),
#  то есть пропорциональна N в квадрете. Таким образом асимптотика сложности алгоритма О большое от N в квадрете
#
#  О большое от N в квадрете означает, что число опреаций не больше чем N в квадрате с точностью до коэффициента


def bubble_sort(a):
    """Сортировка списка А методом пузырька"""
    n = len(a)
    for bypass in range(1, n):
        for k in range(0, n-bypass):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]



def test_sort(sort_algorithm):
    print('Тестируем: ', sort_algorithm.__doc__)
    print('testcase #3: ', end='')
    a = [4, 2, 5, 2, 1]
    a_sorted = [1, 2, 2, 4, 5]
    sort_algorithm(a)
    print("OK" if a == a_sorted else "Failed")


if __name__ == '__main__':
    test_sort(bubble_sort)


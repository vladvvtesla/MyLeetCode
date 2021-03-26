"""

Binare Heap - Sedgewick - w4

Binary tree
Binary tree: Empty or node with links to left and right binary trees.
Complete tree: Perfectly balanced, except for bottom level
Property. The height of a complete tree with N nodes is [lgN]

Binary heap representations.
Binary heap: Array representation of the heap-ordered complete binary tree
Heap-ordered binary tree:
 - Keys in nodes
 - Parent's key no smaller than children's key

Array representations.
 - Indices start at 1
 - Take nodes in level order
 - no explicit links needed

Proposition. The largest key is a[1], which is the root of the binary tree
Proposition. Can use array indices to move through the tree
 - Parent of node at k is at k/2
 - children of node at k are at 2k and 2k+1

Promotion in a heap.  O(lgN)
Exchange key in a child with the key in parent to restore heap order

Demotion in a heap
Exchange key in parent with the key in larger child to restore heap order

Insertion in a heap
Insert. Add a node at the end, then swim it up
Cost. at most 1+lgN compares

Delete the maximum in a heap
Delete max. Exchange root with a node at the end, then sink it down
Cost. At most 2 lg N compares

Priority queues implementation cost summary
order-of-grouth of running time
Implementation  | insert | del max | max
unordered array |   1    |   N     |   N
ordered array   |   N    |   1     |   1
binary heap     |   LogN |  logN   |   1
d-ary heap      |  logd N| d logd N|   1
Fibonachi       |  1     |   log N |   1
impossible      |  1     |    1    |   1

Binary heap consideration
Immutability of keys
 - use immutable keys
Underflow and overflow
 - Underflow: throw an exception if deleting from empty PQ
 - overflow: ad no-arg constructor and use resizing array

Minimum oriented priority queue
 - Replace less() with greater()
 - Implement greater

=====

19.1 Куча   Хирьянов - лекция 19

Структура данных дерево это такая структура, у которого есть корень дерева, у корня есть потомки, а употомков - свои потомки.
Если у каждого потомка не более двух потомков, то это двоичное дерево.

Можно сделать кучу наоборот. В корне будет самое большое число, а далее числа будут убывать. От этого свойства кучи не поменяются.


Куча - это двоичное дерево, у которого три свойства.
1) значение в каждой вершине не больше, чем значение в вершинах его потомков
2) глубина всех листьев отличается не больше чем на единицу
3) последний слой всегда заполняется слева направо без пробелов.

Глубиной называется кратчайший путь от вершинки до корня. Сам корень находится на глубине 0.
Листьями называются вершинки, которые не имеют потомков

5-8-3 не куча, так как 1-е свойство нарушено
Глубина одного листа 1 другого листа  - 2 , тогда второе свойство не нарушено , это куча

Кучи удобно хранить в массиве. Если позиция элемента i, то позиции его потомков легко находятся по формулам для левого и правого потомка
2i+1 и 2i+2
Для нахождения родителя для i-го элемента также простая формула (i-1)//2

   Как реализовать метод вставки в кучу (insert).
Например, хотим вставить 6. Вставляем сразу  на нижний слой в конец кучи. Но ее родитель 7 больше 6,
нарушилось свойство кучи. Меняем местами 6 и 7, 6 переезжает на уровень выше. Снова проверяем, с родителем.
3 меньше 6, поэтому 6 стоит на верном месте. Вставка завершена.
    Достать элемент из кучи. Самый простой метод, это извлечь минимум или максимум из кучи. Но мало достать,
нужно еще удалить. Если просто удалить элемент, все развалится. Правильно  так. Поменять местами корневой
элемент и  самый нижний элемент. А затем элемент оказавшийся в корне спустить как моюно ниже, чтобы соблюсти
все свойства кучи.


Теперь оценим , сколько работают наши функции
_swim: О(log2 n) в худшем случае
_sink: О(log2 n) в худшем случае
    min = O(1)
extract_min О(log2 n)
insert O(log2 n)
Сама куча в памяти занимает O(n)
То есть куча и памяти потребляет немного, и работает относительно быстро

"""

# Implementation

class MinHeap():
    def __init__(self):
        self.a = []                # array for Priority Queue
        self.sz = 0                # Heap size or length of array

    def insert(self, x):
        """Insert item into heap"""
        self.a.append(x)           # O(1)
        self.sz += 1
        self._swim(self.sz - 1)    # O(lgN)

    def peek(self):
        if self.a[0]:
            return self.a[0]
        else:
            return False

    def delMin(self):
        """Return min element and delete it from heap"""
        if not self.sz:
            return None
        min = self.a[0]
        self.a[0],self.a[-1] = self.a[-1],self.a[0]   # put the last item into the root
        self.a.pop(-1)                                # delete last item and resize array
        self.sz -= 1
        self._sink(0)
        return min

    def isEmpty(self):
        return self.sz == 0

    def _swim(self, k):
        """Promotion in a min heap"""
        while k != 0 and self.a[k] <= self.a[(k-1)//2]:
            self.a[k], self.a[(k-1)//2] = self.a[(k-1)//2], self.a[k]
            k = (k-1)//2

    def _sink(self, k):
        """Demotion in a heap"""
        while k+1 <= self.sz:
            j = k  # здесь храним номер позиции с которой будем меняться. В начале запоминаем самого себя.
            if 2*k+1 < self.sz and self.a[2*k+1] < self.a[k]:
                j = 2*k + 1
            if 2*k+2 < self.sz and self.a[2*k+2] < self.a[j]:    # проверим, есть ли правый потомок
                j = 2*k + 2
            if k == j:   # если k не изменился
                break
            else:
                self.a[k],self.a[j] = self.a[j],self.a[k]
                k = j                  # change k for next iteration

def test_heap():
    heap = MinHeap()
    print(heap.isEmpty(), ': should be True')
    heap.insert(5)
    print(heap.peek(), ': should be 5')
    heap.insert(3)
    heap.insert(7)
    print(heap.peek(), ': should be 3')
    print(heap.isEmpty(), ': should be False')

    print(heap.delMin(), ': should be 3')

    heap.insert(2)
    heap.insert(9)
    print(heap.delMin(), ': should be 2')
    print(heap.delMin(), ': should be 5')
    print(heap.delMin(), ': should be 7')
    print(heap.isEmpty(), ': should be False')
    print(heap.delMin(), ': should be 9')
    print(heap.isEmpty(), ': should be True')


if __name__ == '__main__':
    test_heap()
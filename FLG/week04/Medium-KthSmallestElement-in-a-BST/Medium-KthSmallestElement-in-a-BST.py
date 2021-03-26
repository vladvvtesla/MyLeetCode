"""
230. Kth Smallest Element in a BST

# Main idea
1. Create Sized MaxHeap with capacity k
2. Fill MaxHeap with nodes from BST
3. Return Kth item from MaxHeap's


Tine complexity:            O(N log K)
inorder Traversal of BST:   N
insert N item into heap:    N log K
del N item from heap:       N log K
peek from heap:             1

Space Complecity:   O(N + K)
N for BST
K for MaxHeap


Runtime: 176 ms, faster than 6.10% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18.5 MB, less than 15.00% of Python3 online submissions for Kth Smallest Element in a BST.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class MaxHeap():
    def __init__(self):
        self.a = []                # array for Priority Queue
        self.sz = 0                # Heap size or length of array

    def insert(self, x):
        """Insert item into heap"""
        self.a.append(x)           # O(1)
        self.sz += 1
        self._swim(self.sz - 1)    # O(lgN)

    def peek(self):
        if self.a:
            return self.a[0]
        else:
            return False

    def delMax(self):
        """Return max element and delete in from heap"""
        if not self.sz:
            return None
        max = self.a[0]
        self.a[0],self.a[-1] = self.a[-1],self.a[0]   # put the last item into the root
        self.a.pop(-1)                                # delete last item and resize array
        self.sz -= 1
        self._sink(0)
        return max

    def isEmpty(self):
        return self.sz == 0

    def _swim(self, k):
        """Promotion in a heap"""
        while k != 0 and self.a[k] >= self.a[(k-1)//2]:
            self.a[k], self.a[(k-1)//2] = self.a[(k-1)//2], self.a[k]
            k = (k-1)//2

    def _sink(self, k):
        """Demotion in a heap"""
        while k+1 <= self.sz:
            j = k  # здесь храним номер позиции с которой будем меняться. В начале запоминаем самого себя.
            if 2*k+1 < self.sz and self.a[2*k+1] > self.a[k]:
                j = 2*k + 1
            if 2*k+2 < self.sz and self.a[2*k+2] > self.a[j]:    # проверим, есть ли правsй потомок
                j = 2*k + 2
            if k == j:   # если k не изменился
                break
            else:
                self.a[k],self.a[j] = self.a[j],self.a[k]
                k = j                  # change k for next iteration


class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.count = 1         # number of nodes in subtree including itself

class BST:
    def __init__(self):
        self.root = None

    def put(self, key, val):
        """Put Node or create new"""
        if self.root:
            self._put(self.root, key, val)
        else:
            self.root = Node(key, val)
            # self.root.count += 1

    def _put(self, x, key, val):
        """x: Node object"""
        if not x:                     # If child
            return Node(key, val)

        if key < x.key:
            x.left = self._put(x.left, key, val)
        elif key > x.key:
            x.right = self._put(x.right, key, val)
        else:
            x.val = val
        x.count = 1 + self._size(x.left) + self._size(x.right)
        return x

    def size(self):
        """ Total number of nodes in the tree"""
        return self._size(self.root)

    def _size(self, x):
        """Return number of nodes in subtree"""
        if x is None:
            return 0
        else:
            return x.count


class Solution:
    def kthSmallest(self, root, k):

        def _inorderTraversal(x):
            """
            A function to do inorder tree traversal  (Left, Root, Right)
            :param x:  root node
            :return: list
            """
            return (_inorderTraversal(x.left) + [x.val] + _inorderTraversal(x.right)) if x else []

        inorder = _inorderTraversal(root)   # list of the all values of the BST

        heap = MaxHeap()
        for v in inorder:
            heap.insert(v)
            if heap.sz > k:              # Insert items into a Sized MaxHeap
                heap.delMax()            # the heap contains K smallest items of the stream

        while heap.sz != k:              # extract items from heap excluding the last K items
            heap.delMax()

        return heap.peek()               # return the last item in the heap



def test_kthSmallest():

    inp = [([3,1,4,None,2], 1), ([5,3,6,2,4,None,None,1], 3)]
    out = [1, 3]

    for i in range(len(inp)):
        bst = BST()
        [bst.put(v, v) for k, v in enumerate(inp[i][0]) if v is not None]
        sol = Solution()
        test_res = sol.kthSmallest(bst.root, inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_kthSmallest()
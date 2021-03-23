"""
Binary search trees  - Sedgewick - w4

Definition. A BST is a  binary tree in symmetric order.
Symmetric order. Each node has a key, and every  node’s key is:
 - Larger than all keys in its left subtree.
 - Smaller than all keys in its right subtree.

Inorder traversal.
- Traverse left subtree.
- Enqueue key.
- Traverse right subtree.

Property.I norder traversal of a BST yields keys in ascending order

Symbol Tables Implementation:
        | Guarantee        | Average case         |
        | Search  | Insert | Search   | Insert    |
BST     | N       |   N    | 1.39 lgN | 1.39 lgN  |
"""

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

    def get(self, key):
        """ Return value corresponding to given key, or None if no such key."""
        x = self.root
        while x is not None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.val
        return None

    def size(self):
        """ Total number of nodes in the tree"""
        return self._size(self.root)

    def _size(self, x):
        """Return number of nodes in subtree"""
        if x is None:
            return 0
        else:
            return x.count

    def floor(self, key):
        """Floor. Largest key <= a given key.
        return key"""
        x = self._floor(self.root, key)
        if x is None:
            return None
        return x.key

    def _floor(self, x, key):
        """return Node"""
        if x is None:
            return None
        if key == x.key:
            return x
        if key < x.key:
            return self._floor(x.left, key)
        t = self._floor(x.right, key)
        if t is not None:
            return t
        else:
            return x

    def ceiling(self, key):
        """Ceiling. Smallest key ≥ a given key."""
        pass

    def rank(self, key, x):
        """Rank. How many keys < k ?"""
        if x is None:
            return 0
        if key < x.key:
            return self.rank(key, x.left)
        elif key > x.key:
            return 1 + self._size(x.left) + self.rank(x.left, key)
        else:
            return self._size(x.left)

    def deleteMin(self, x):
        """
        Deleting the minimum:
        - Go left until finding a node with a null left link.
        - Replace that node by its right link.
        - Update subtree counts.
        """
        if x.left is None:
            return x.right
        x.left = self.deleteMin(x.left)
        x.count = 1 + self._size(x.left) + self._size(x.right)
        return x

    def delete(self, x, key):
        """Hibbard deletion - Sedgewick w4"""
        if x is None:
            return None
        if key < x.key:                         # search for key
            x.left = self.delete(x.left, key)
        elif key > x.key:                        # search for key
            x.right = self.delete(x.right, key)
        else:
            if x.right is None:
                return (x.left)                  # no right child
            if x.rleft is None:
                return (x.right)                 # no left child

            t = x
            x = min(t.right)
            x.right = self.deleteMin(t.right)
            x.left = t.left                                   # replace with successor
        x.count = 1 + self._size(x.left) + self._size(x.right)  # update subtree counts
        return x

    def inorderTraversal(self, x):
        """
        A function to do inorder tree traversal  (Left, Root, Right)
        :param x:  root node
        :return: list
        """
        return (self.inorderTraversal(x.left) + [x.val] + self.inorderTraversal(x.right)) if x else []

    def postorderTraversal(self, x):
        """
        A function to do postorder tree traversal (Left, Right, Root)
        :param x:  root node
        """
        return (self.postorderTraversal(x.left) + self.postorderTraversal(x.right) + [x.val]) if x else []

    def preorderTraversal(self, x):
        """
        A function to do preorder tree traversal (Root, Left, Right)
        :param x: root Node
        """
        return ([x.val] + self.preorderTraversal(x.left) + self.preorderTraversal(x.right)) if x else []


    def levelorderTraversal(self, x):
        # Create an empty list for result
        res = []

        # Base Case
        if x is None:
            return

        # Create an empty queue for level order traversal
        queue = []

        # Enqueue Root and initialize height
        queue.append(x)

        while (len(queue) > 0):

            # Print front of queue and remove it from queue
            print(queue[0].val)
            res.append(queue[0].val)
            node = queue.pop(0)

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)

        return res

def test_BST():
    """
    bst = BST()
    print(bst.size(), ': should be 0')
    # print(bst.isEmpty(), ': should be True')
    bst.put(0, 5)
    print(bst.size(), ': should be 1')
    bst.put(1, 3)
    print(bst.size(), ': should be 2')
    bst.put(2, 7)
    print(bst.size(), ': should be 3')
    bst.put(2, 7)
    print(bst.size(), ': should be 3')
    print()
    """

def test_BST_put_1():
    bst = BST()
    bst.put(0, 5)
    test_res = bst.size()
    # print('test_res', test_res)
    print("Test", 1, ': put_1', "OK\n" if test_res == 1 else "Failed\n")

def test_BST_put_2():
    bst = BST()
    bst.put(0, 5)
    bst.put(1, 3)
    bst.put(2, 7)
    bst.put(2, 7)
    test_res = bst.size()
    print("Test", 2, ': put_2', "OK\n" if test_res == 3 else "Failed\n")

def test_BST_get_1():
    """
           0 (5)
         /   \
             1 (3)
    """
    bst = BST()
    bst.put(0, 5)
    bst.put(1, 3)
    test_res = bst.get(1)
    # print('test_res', test_res)
    print("Test", 3, ': get_1', "OK\n" if test_res == 3 else "Failed\n")

def test_BST_get_2():
    bst = BST()
    bst.put(0, 5)
    bst.put(1, 3)
    test_res = bst.get(30)
    # print('test_res', test_res)
    print("Test", 4, ': get_2', "OK\n" if test_res is None else "Failed\n")

def test_BST_inorderTraversal():
    bst = BST()
    arr = [4,2,5,1,3]
    [bst.put(v,v) for k,v in enumerate(arr)]
    test_res = bst.inorderTraversal(bst.root)
    print('test_res', test_res)
    print("Test", 5, ': inorderTraversal :', "OK\n" if test_res == [1,2,3,4,5] else "Failed\n")

def test_BST_postorderTraversal():
    bst = BST()
    arr = [4,2,5,1,3]
    [bst.put(v,v) for k,v in enumerate(arr)]
    test_res = bst.postorderTraversal(bst.root)
    print('test_res', test_res)
    print("Test", 6, ': postorderTraversal :', "OK\n" if test_res == [1,3,2,5,4] else "Failed\n")

def test_BST_preorderTraversal():
    bst = BST()
    arr = [4,2,5,1,3]
    [bst.put(v,v) for k,v in enumerate(arr)]
    test_res = bst.preorderTraversal(bst.root)
    print('test_res', test_res)
    print("Test", 7, ': preorderTraversal :', "OK\n" if test_res == [4,2,1,3,5] else "Failed\n")

def test_BST_levelorderTraversal():
    bst = BST()
    arr = [4,2,5,1,3]
    [bst.put(v,v) for k,v in enumerate(arr)]
    test_res = bst.levelorderTraversal(bst.root)
    print('test_res', test_res)
    print("Test", 8, ': levelorderTraversal :', "OK\n" if test_res == [4,2,5,1,3] else "Failed\n")

def test_BST_levelorderTraversal_1():
    bst = BST()
    arr = [4,2,5,1,3,9]
    [bst.put(v,v) for k,v in enumerate(arr)]
    test_res = bst.levelorderTraversal(bst.root)
    print('test_res', test_res)
    print("Test", 9, ': levelorderTraversal_1 :', "OK\n" if test_res == [4,2,5,1,3,None,9] else "Failed\n")


if __name__ == '__main__':
    # test_BST()
    test_BST_put_1()
    test_BST_put_2()
    test_BST_get_1()
    test_BST_get_2()
    test_BST_inorderTraversal()
    test_BST_postorderTraversal()
    test_BST_preorderTraversal()
    test_BST_levelorderTraversal()
    test_BST_levelorderTraversal_1()
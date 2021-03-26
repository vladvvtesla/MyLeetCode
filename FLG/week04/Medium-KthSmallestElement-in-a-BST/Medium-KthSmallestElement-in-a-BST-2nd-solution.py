"""
230. Kth Smallest Element in a BST

# Main idea
1. inorderTraversal of BST -> into list
3. Return K-1 th item from list


Tine complexity:            O(N)
inorder Traversal of BST:   N
get item by index:          1

Space Complexity:   O(N)
N for BST
N for list


Runtime: 56 ms, faster than 37.88% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18.3 MB, less than 14.85% of Python3 online submissions for Kth Smallest Element in a BST.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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

        return inorder[k-1]


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
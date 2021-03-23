"""
700. Search in a Binary Search Tree

Main Idea:
Equal to get() method of BST

Time Complexity:  O(logN)

Space Complexity:  O(N)
all the N nodes of the tree

Runtime: 76 ms, faster than 52.91% of Python3 online submissions for Search in a Binary Search Tree.
Memory Usage: 16.2 MB, less than 60.93% of Python3 online submissions for Search in a Binary Search Tree.

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

    def preorderTraversal(self, x):
        """
        A function to do preorder tree traversal (Root, Left, Right)
        :param x: root Node
        """
        return ([x.val] + self.preorderTraversal(x.left) + self.preorderTraversal(x.right)) if x else []


class Solution:
    def searchBST(self, root, val):        # O(logN)
        x = root
        while x is not None:
            if val < x.val:
                x = x.left
            elif val > x.val:
                x = x.right
            else:
                return x
        return None

def test_searchBST():
    inp = [([4,2,7,1,3], 2), ([4,2,7,1,3], 5)]
    out = [[2,1,3],[]]

    for i in range(len(inp)):
        bst = BST()
        [bst.put(v, v) for k, v in enumerate(inp[i][0])]
        sol = Solution()
        node = sol.searchBST(bst.root, inp[i][1])
        test_res = bst.preorderTraversal(node)
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_searchBST()
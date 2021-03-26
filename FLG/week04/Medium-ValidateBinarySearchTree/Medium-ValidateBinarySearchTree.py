"""
98. Validate Binary Search Tree

"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isValidBST(self, root):
        if not root:
            return True

        top = root.val
        if root.left and root.left.val >= root.val and root.left.val >= top:
            return False
        if root.right and root.right.val <= root.val and root.right.val <= top:
            return False
        return self._isValidBST(root.left, top) and self._isValidBST(root.right, top)

    def _isValidBST(self, x, top):
        if not x:                          # Case Base
            return True

        if x.left and x.left.val >= x.val and x.left.val >= top:
            return False
        if x.right and x.right.val <= x.val and x.right.val <= top:
            return False
        # true if both subtree are valid bst
        return self._isValidBST(x.left, top) and self._isValidBST(x.right, top)


def test_isValidBST():
    # [2,1,3]
    x = TreeNode(2)
    x.left = TreeNode(1)
    x.right = TreeNode(3)
    sol = Solution()
    test_res = sol.isValidBST(x)
    print('test_res', test_res)
    print("Test", 1, ":", "OK\n" if test_res == True else "Failed\n")

    # [5,1,4,null,null,3,6]
    x = TreeNode(5)
    x.left = TreeNode(1)
    x.right = TreeNode(5)
    x.right.left = TreeNode(3)
    x.right.left = TreeNode(6)
    sol = Solution()
    test_res = sol.isValidBST(x)
    print('test_res', test_res)
    print("Test", 2, ":", "OK\n" if test_res == False else "Failed\n")

    # [1,1]
    x = TreeNode(1)
    x.left = TreeNode(1)
    sol = Solution()
    test_res = sol.isValidBST(x)
    print('test_res', test_res)
    print("Test", 3, ":", "OK\n" if test_res == False else "Failed\n")

    # [5,4,6,null,null,3,7] : Expexted False
    x = TreeNode(5)
    x.left = TreeNode(4)
    x.right = TreeNode(6)
    x.right.left = TreeNode(3)
    x.right.right = TreeNode(7)
    sol = Solution()
    test_res = sol.isValidBST(x)
    print('test_res', test_res)
    print("Test", 4, ":", "OK\n" if test_res == False else "Failed\n")




if __name__ == '__main__':
    test_isValidBST()
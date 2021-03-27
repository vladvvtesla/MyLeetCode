"""
98. Validate Binary Search Tree


Time Complexity: O(N)
Compare each N node to x.val and root.val

Space Complexity: O(N)
N nodes

Runtime: 40 ms, faster than 88.61% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.3 MB, less than 79.93% of Python3 online submissions for Validate Binary Search Tree.

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
            return False

        if root.left:
            if root.left.val >= root.val:
                return False
            left_res = self._isValidBST(root.left, min=float('-inf'), max=root.val)
        else:
            left_res = True

        if root.right:
            if root.right.val <= root.val:
                return False
            right_res = self._isValidBST(root.right, min=root.val, max=float('inf'))
        else:
            right_res = True

        return left_res and right_res


    def _isValidBST(self, x, min, max):

        if x.left:
            if (x.left.val >= x.val) or (x.left.val <= min):
                 return False
            left_res = self._isValidBST(x.left, min=min, max=x.val)
        else:
            left_res = True

        if x.right:
            if (x.right.val <= x.val) or (x.right.val >= max):
                return False
            right_res = self._isValidBST(x.right, min=x.val, max=max)
        else:
            right_res = True

        return left_res and right_res


def test_isValidBST():
    # [2,1,3] :  Expected True
    x = TreeNode(2)
    x.left = TreeNode(1)
    x.right = TreeNode(3)
    sol = Solution()
    test_res = sol.isValidBST(x)
    print('test_res', test_res)
    print("Test", 1, ":", "OK\n" if test_res == True else "Failed\n")

    # [5,1,4,null,null,3,6] :  Expected False
    x = TreeNode(5)
    x.left = TreeNode(1)
    x.right = TreeNode(4)
    x.right.left = TreeNode(3)
    x.right.left = TreeNode(6)
    sol = Solution()
    test_res = sol.isValidBST(x)
    print('test_res', test_res)
    print("Test", 2, ":", "OK\n" if test_res == False else "Failed\n")

    # [1,1] :  Expected False
    x = TreeNode(1)
    x.left = TreeNode(1)
    sol = Solution()
    test_res = sol.isValidBST(x)
    print('test_res', test_res)
    print("Test", 3, ":", "OK\n" if test_res == False else "Failed\n")

    # [5,4,6,null,null,3,7] : Expected False
    x = TreeNode(5)
    x.left = TreeNode(4)
    x.right = TreeNode(6)
    x.right.left = TreeNode(3)
    x.right.right = TreeNode(7)
    sol = Solution()
    test_res = sol.isValidBST(x)
    print('test_res', test_res)
    print("Test", 4, ":", "OK\n" if test_res == False else "Failed\n")

    # [32,26,47,19,null,null,56,null,27] :  Expected False
    x = TreeNode(32)
    x.left = TreeNode(26)
    x.right = TreeNode(47)
    x.left.left = TreeNode(19)
    x.right.right = TreeNode(56)
    x.left.left.right = TreeNode(27)
    sol = Solution()
    test_res = sol.isValidBST(x)
    print('test_res', test_res)
    print("Test", 5, ":", "OK\n" if test_res == False else "Failed\n")

    # [1, null, 1] :  Expected False
    x = TreeNode(1)
    x.right = TreeNode(1)
    sol = Solution()
    test_res = sol.isValidBST(x)
    print('test_res', test_res)
    print("Test", 6, ":", "OK\n" if test_res == False else "Failed\n")



if __name__ == '__main__':
    test_isValidBST()
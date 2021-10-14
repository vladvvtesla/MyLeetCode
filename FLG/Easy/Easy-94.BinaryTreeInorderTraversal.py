"""
Easy 94. Binary Tree Inorder Traversal

Time complexity: O(n)

Space complexity: O(log n)

Runtime: 24 ms, faster than 96.66% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14 MB, less than 98.66% of Python3 online submissions for Binary Tree Inorder Traversal.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        cur = root
        if cur is None:
            return []
        res = self.inorderTraversal(cur.left) + [cur.val] + self.inorderTraversal(cur.right)

        return res

def test_Solution1():
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)

    sol = Solution()
    test_res = sol.inorderTraversal(t)
    print('test_res', test_res)
    print("Test", 1, ":", "OK\n" if test_res == [1,3,2] else "Failed\n")

def test_Solution2():

    sol = Solution()
    test_res = sol.inorderTraversal(None)
    print('test_res', test_res)
    print("Test", 2, ":", "OK\n" if test_res == [] else "Failed\n")

def test_Solution3():
    t = TreeNode(1)

    sol = Solution()
    test_res = sol.inorderTraversal(t)
    print('test_res', test_res)
    print("Test", 3, ":", "OK\n" if test_res == [1] else "Failed\n")

def test_Solution4():
    t = TreeNode(1)
    t.left = TreeNode(2)

    sol = Solution()
    test_res = sol.inorderTraversal(t)
    print('test_res', test_res)
    print("Test", 4, ":", "OK\n" if test_res == [2,1] else "Failed\n")

def test_Solution5():
    t = TreeNode(1)
    t.right = TreeNode(2)

    sol = Solution()
    test_res = sol.inorderTraversal(t)
    print('test_res', test_res)
    print("Test", 5, ":", "OK\n" if test_res == [1,2] else "Failed\n")


if __name__ == '__main__':
     test_Solution1()
     test_Solution2()
     test_Solution3()
     test_Solution4()
     test_Solution5()
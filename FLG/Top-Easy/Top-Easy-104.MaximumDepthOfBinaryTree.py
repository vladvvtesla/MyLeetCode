"""

Top-Easy-104.MaximumDepthOfBinaryTree

Runtime: 44 ms, faster than 55.69% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.2 MB, less than 40.16% of Python3 online submissions for Maximum Depth of Binary Tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

def test_height():
    t = TreeNode(1)
    t.left = TreeNode(4)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)

    sol = Solution()
    test_res = sol.maxDepth(t)
    print('test_res', test_res)
    print("Test", 2, ":", "OK\n" if test_res == 3 else "Failed\n")



if __name__ == '__main__':
    test_height()







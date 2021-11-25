# Definition for a binary tree node.

# Runtime: 204 ms, faster than 79.67% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 22.2 MB, less than 69.93% of Python3 online submissions for Range Sum of BST.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return self.helper(root, low, high, 0)

    def helper(self, node, left, right, total):
        if node is None:
            return total

        if left <= node.val <= right:
            total += node.val
            total = self.helper(node.left, left, right, total)
            total = self.helper(node.right, left, right, total)

        if node.val < left:
            total = self.helper(node.right, left, right, total)

        if node.val > right:
            total = self.helper(node.left, left, right, total)

        return total



def test_rangeSumBST():
    inputs = [([10,5,15,3,7,None,18],7,15), ([10,5,15,3,7,13,18,1,None,6],6,10)]
    out = [32, 23]
    sol = Solution()
    for i in range(len(inputs)):
        print(len(inputs))
        print(inputs[0][0])
        print(inputs[0][1])
        test_res = sol.rangeSumBST(inputs[i][0], inputs[i][1], inputs[i][2])
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")


if __name__ == '__main__':
    test_rangeSumBST()
"""
1. Two Sum  (Top-Easy)

Main Idea:
Two pointers

Time complexity: O(n^2)

Space complexity: O(n^2)

Runtime: 4036 ms, faster than 24.56% of Python3 online submissions for Two Sum.
Memory Usage: 14.7 MB, less than 92.30% of Python3 online submissions for Two Sum.
"""

class Solution:
    def twoSum(self, nums, target):
        for k in range(1, len(nums)+1):
            for j in range(k):
                if nums[k] + nums[j] == target:
                    return [j, k]

def test_Solution():

    inp = [([2,7,11,15], 9), ([3,2,4], 6), ([3,3], 6)]
    out = [[0,1],[1,2],[0,1]]

    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.twoSum(inp[i][0],inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_Solution()
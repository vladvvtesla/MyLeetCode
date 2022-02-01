"""
169. Majority Element (Easy but in Top-Medium List may be due tu follow-up)

Main Idea.
Boyer Moore Voting Algorithm)

Time complexity: O(n)

Space Complexity: O(1)



Space complexity: O (N*M)
"""
class Solution:
    def majorityElement(self, nums):
        idx = 0
        count = 1
        for k in range(len(nums)):
            if nums[idx] == nums[k]:
                count += 1
            else:
                count -= 1
            if count == 0:
                idx = k
                count = 1
        return nums[idx]


def test_solution():
    inp = [ [3,2,3],
            [2,2,1,1,1,2,2],
            [2],
            [2,2,1,1,1],
            [1,1,1,2,2],
            [1, 2, 1, 1, 2],
            [1,2,3,1,2,3,3,3,2]
          ]
    out = [3, 2, 2, 1, 1, 1, 3]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.majorityElement(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()


if __name__ == '__main__':
    test_solution()

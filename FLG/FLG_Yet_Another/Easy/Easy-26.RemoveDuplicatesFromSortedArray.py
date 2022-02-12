"""
26. Remove Duplicates from Sorted Array (Easy)

Main Idea.
Two pointers
start = 0
cur = 0
1) Пройтись по всему nums:
    если nums[cur] == nums[start]:
        идем дальше
    если nums[cur] != nums[start]:
        а) то start переместить вперед на 1
        б) обменять значения nums[cur] и nums[start]
Вернуть start+1


Time complexity: O(n)

Space complexity: O(1)

Runtime: 88 ms, faster than 82.15% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.5 MB, less than 78.95% of Python3 online submissions for Remove Duplicates from Sorted Array.

"""
class Solution:
    def removeDuplicates(self, nums) -> int:
        st = 0
        for cur, v in enumerate(nums):
            if nums[cur] != nums[st]:
                st += 1
                nums[cur], nums[st] = nums[st], nums[cur]
        return st + 1


def test_solution():
    inp = [ [1,1,2],
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            [1]
          ]
    out = [2,5,1]
    # inp = [[1,1,2]]
    # out = [2]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.removeDuplicates(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()




if __name__ == '__main__':
    test_solution()

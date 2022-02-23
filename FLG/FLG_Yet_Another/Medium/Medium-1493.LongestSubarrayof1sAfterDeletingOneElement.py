"""
1493. Longest Subarray of 1's After Deleting One Element (Medium)

Main Idea.
Попробуем свести к задаче с последовательностью 1ц при замене одного 0 на 1
Только здесь возвращаем на 1 меньше, так как
считаем, что после замены 0 на 1, мы это значение еще и удалили
1 1 0 1 0 1 1 1 1
      l           r
Так же нужно учесть, начинается массив с 1 или с 0, важно для edge case

Time complexity: O(n)

Space complexity: O(1)

Runtime: 639 ms, faster than 24.62% of Python3 online submissions for Longest Subarray of 1's After Deleting One Element.
Memory Usage: 16.6 MB, less than 62.50% of Python3 online submissions for Longest Subarray of 1's After Deleting One Element.
"""
class Solution:
    def longestSubarray(self, nums) -> int:
        # if nums == [1]: return 0     # Edge case
        res = 0
        lo = r = 0
        credit = 1  # кредит на замену
        while r < len(nums):                     # 1 0 0 0 0
            if credit >= 0:                      # lr
                if nums[r] == 0:                 # credit = 1
                    credit -= 1                  # res = 0
                res = max(res, r - lo + nums[r] - 1) # учесть начальный 0  или 1
                r += 1
            else:
                #  сюда попадаем если r прошел второй 0 и остановился
                credit += (1 - nums[lo])
                lo += 1
        return res


def test_solution():
    inp = [ [1,1,0,1],
            [0,1,1,1,0,1,1,0,1],
            [1, 1, 1],
            [0, 1, 1, 1],
            [1],
            [1, 0, 0, 0, 0],
            [0, 0, 0]
            ]
    out = [3,5,2,3,0, 1, 0]
    # inp = [[1,1,0,1]]
    # out = [3]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.longestSubarray(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")




if __name__ == '__main__':
    test_solution()

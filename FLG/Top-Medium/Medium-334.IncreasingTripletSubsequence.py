"""
Medium 334. Increasing Triplet Subsequence

Main Idea:
Бежим по списку и заполняем корзину из 3 чисел. min, mid, max
сначала заполняем min и max
Как только нашли еще одно число больше старого  max,
И все три числа найдены -> return True

Для экономии места min можно хранить в nums[0]

Time Complexity: O(n)

Space complexity: O(n) plus extra space O(1) for max

Runtime: 592 ms, faster than 58.63% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 25.3 MB, less than 36.39% of Python3 online submissions for Increasing Triplet Subsequence.
"""
class Solution:
    def increasingTriplet(self, nums):
        min = max = None
        for el in nums:
            if min is None or el < min:
                min = el
            elif max is None or el < max:
                if el > min:
                    max = el
            elif el > max:
                return True
        return False


def test_solution():
    inp = [ [1,2,3,4,5],
            [5,4,3,2,1],
            [2, 1, 5, 0, 4, 6],
            [0, -1, 0, 10],
            [0, -1, 2, 10],
            [20, 100, 10, 12, 5, 13],
            [20, 100, 10, 200, 300],
            [20,100,10,12,5,13],
            [1,1,-2,6]]
    out = [True, False, True, True, True, True, True, True, False]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.increasingTriplet(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()


if __name__ == '__main__':
    test_solution()

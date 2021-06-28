"""
303. Easy - Range Sum Query - Immutable

Main Idea: DP
Explonation:
https://www.youtube.com/watch?v=ZMOFmHBVEcg&list=PLiQ766zSC5jM2OKVr8sooOuGgZkvnOCTI&index=4
1. построить вспомогательный список cache
        cache[k+1] = cache[k] + self.nums[k]
2. Для того, чтобы получить сумму значений от 0 до 3,
нам нужно за О(1)  вытащить значение cache[3]
3. Для того, чтобы получить сумму значений от 2 до 3,
из полной суммы до 3 вычесть часть суммы до 1,
то есть из cache[3] вычесть cache[2-1]


Time complexity: O(N)
O(N) for making a cache
O(1) to get sum

Space complexity: O(N)
O(N) for array
O(N) extra space for cache

Runtime: 72 ms, faster than 92.92% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 17.7 MB, less than 45.67% of Python3 online submissions for Range Sum Query - Immutable.
"""
class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.cache = [0]*(len(self.nums)+1)
        for k in range(len(self.nums)):
            self.cache[k+1] = self.cache[k] + self.nums[k]

    def sumRange(self, left, right):
        if left == 0:
            return self.cache[right+1]
        else:
            return self.cache[right+1] - self.cache[left]

    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(left,right)

def test_longestCommonSubsequence():
    inp = [
            [[-2, 0, 3, -5, 2, -1], [0, 2], [2, 5], [0, 5]],
            [[-4, -5], [0, 0], [1, 1], [0, 1]]
            ]
    out = [[None, 1, -1, -3],
           [None,-4, -5, -9]]

    for i in range(len(inp)):
        inpArr = NumArray(inp[i][0])
        test_res = [
            None,
            inpArr.sumRange(inp[i][1][0],inp[i][1][1]),
            inpArr.sumRange(inp[i][2][0],inp[i][2][1]),
            inpArr.sumRange(inp[i][3][0],inp[i][3][1])
            ]
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_longestCommonSubsequence()
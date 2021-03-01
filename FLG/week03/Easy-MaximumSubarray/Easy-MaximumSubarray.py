"""
Easy -  Maximum Subarray

Runtime: 64 ms, faster than 78.58% of Python3 online submissions for Maximum Subarray.
Memory Usage: 15.1 MB, less than 15.44% of Python3 online submissions for Maximum Subarray.


-- Using Dynamic Programming --
Perfect explanatioin: Igor Kleiner -  https://youtu.be/-9xQVtqWbRQ

There are several methods for solving this problem
1) Recursion
2) Divide-and-conquer
3) Dynamic programming


[-2,1,-3,4,-1,2,1,-5,4]
[A1, A2, ..., Ai, ..., An]

F+(i)    maximum summ of subbarray from i to n, including Ai
F-(i)    maximum summ of subbarray from i to n, excluding Ai

Answer: F1 = max[F+(1), F-(1)]
Base cases:  F+(n) = An, F-(n) = 0
Functional Equation:  F+(i) = Ai + max[F+(i+1), 0]
                      F-(i) =      max[F+(i+1), F-(i+1)]


F+(n) <- F+(n-1) <- F+(n-2) <- ... <- F+(1)     :  O (N)
F-(n) <- F-(n-1) <- F-(n-2) <- ... <- F-(1)     :  O (N)
and
F1 = max[F+(1), F-(1)]

F+(i) = Ai + max[F+(i+1), 0]
Zero, because we will ignore negative numbers


[5, -3, 6, -7, 6]`

A1 | A2 | A3 | A4 | A5 |      A
 5 | -3 |  6 | -7 |  6 |

 8 |  3 |  6 | -1 |  6 |       F+(n)
 6 |  6 |  6 | 6  |  0 |       F-(n)

 F1 = max[8, 6] = 8    [5, -3, 6]


Time complexity:  O ( N )
Space complexity: O ( const )
"""

class Solution:
    def maxSubArray(self, nums):

        import math

        n = len(nums)
        f_plus = [0]*n
        f_minus = [0]*n

        f_plus[-1] = nums[-1]                 # Basic case
        f_minus[-1] = -math.inf               # Basic case

        for i in range(n-2, -1, -1):          # n=5 ==> 4th we know, we'll fill 3,2,1,0
            f_plus[i] = nums[i] + max(f_plus[i+1], 0)
            f_minus[i] = max(f_plus[i+1], f_minus[i+1])

        res = max(f_plus[0], f_minus[0])

        return res


def test_maxSubArray():
    inp = [[5,-3,6,-7,6], [-2,1,-3,4,-1,2,1,-5,4], [1], [0], [-1], [-100000], [-100,1,1,1,1,1,-5] ]
    out = [8, 6, 1, 0, -1, -100000, 5]
    sol = Solution()
    for k,item in enumerate(inp,1):
        test_res = sol.maxSubArray(item)
        print(test_res)
        print("Test", k, ":", "OK" if test_res == out[k-1] else "Failed")
        print()

if __name__ == '__main__':
    test_maxSubArray()
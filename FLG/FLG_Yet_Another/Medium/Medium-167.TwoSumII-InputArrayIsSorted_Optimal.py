"""
167. Two Sum II - Input Array Is Sorted (Medium)

Main Idea.
Two Pointers

1) Start = 0, End = len(nums) - 1
2) check nums[start] + nums[end]  == tar
3) If <
   increment Start
4) elif >
   Decrement End
5) else:
     we found the solution

Time complexity: O(N)

Space complexity: O(1)

Runtime: 233 ms, faster than 6.35% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage: 14.9 MB, less than 7.25% of Python3 online submissions for Two Sum II - Input Array Is Sorted.

"""
class Solution:
    def twoSum(self, nums, tar):
        l, r = 0, len(nums) - 1

        while r >= l:
            res = nums[r] + nums[l]
            if res == tar:
                return [l+1, r+1]
            elif res > tar:
                r -= 1
            else:
                l += 1


def test_solution():
    inp = [ ([2,7,11,15], 9),
            ([2,3,4], 6),
            ([-1,0], -1),
            ]
    out = [[1,2],
           [1,3],
           [1,2]]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.twoSum(inp[i][0], inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()




if __name__ == '__main__':
    test_solution()

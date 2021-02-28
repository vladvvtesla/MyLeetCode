"""
Easy -  Maximum Subarray

Time complexity:
Space complexity:
"""



class Solution:
    def maxSubArray(self, nums):
        cur = nums[0]  # current max sum
        glo = nums[0]  # global max sum

        for idx, item in enumerate(nums):
            if idx == 0:                    #  pass the first item
                continue

            new_cur = cur + item

            if new_cur >= cur:
                cur = new_cur
            else:
                cur = item

            glo = max(cur, glo)

        return glo


def test_maxSubArray():
    inp = [[-2,1,-3,4,-1,2,1,-5,4], [1], [0], [-1], [-100000], [-100,1,1,1,1,1,-5]]
    out = [6, 1, 0, -1, -100000, 0]
    sol = Solution()
    for k,item in enumerate(inp,1):
        test_res = sol.maxSubArray(item)
        print(test_res)
        print("Test", k, ":", "OK" if test_res == out[k-1] else "Failed")
        print()

if __name__ == '__main__':
    test_maxSubArray()
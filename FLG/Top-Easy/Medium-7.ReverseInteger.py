"""
7. Reverse Integer (Medium but in the Top-easy list)

Main Idea:
1. Number to digits into auxiliary arr
2. Digit to number

Time Complexity:  O(n)

Space Complexity: extra space O(n)  for auxiliary array.  N is a number of digits

Runtime: 36 ms, faster than 48.62% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.2 MB, less than 46.30% of Python3 online submissions for Reverse Integer.
"""

class Solution:
    def reverse(self, x):
        sign = True if x < 0 else False              # Take into account sign
        if x < 0: x *= -1                            # delete sign

        ilist = []                                   # Number to digits.  O(n) N is number of digits
        while x:
            ilist.append(x % 10)
            x //= 10

        res = 0
        n = len(ilist)
        for k in range(n):                           # O(n)
            if ilist[k] != '0':                      # skip heading and all zeroes  in [0, 0, 0, 2, 1]
                summand = ilist[k] * (10**(n - k - 1))
                if 2147483648 - abs(res) < summand:     # res + summand > 2^32
                    return 0
                else:
                    res += summand   # get result  2*10^1 + 1*10^0

        if sign: res *= -1                           # return  sign

        return res


def test_solution():
    inp = [123, -123, 120, 0, -120, -12000, 1534236469, -1534236469, 1563847412]
    # inp = [-120]
    out = [321, -321, 21, 0, -21, -21, 0, 0, 0]
    # out = [-21]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.reverse(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
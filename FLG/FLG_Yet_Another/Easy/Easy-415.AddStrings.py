"""
415. Add Strings (415)

Main Idea.
1) создать фнкцию для конвертации строки в число
2) вернуть str(to_digit(num1) + to_digit(num2))

Time complexity: O(N)

Space complexity: no extra space

Runtime: 777 ms, faster than 5.04% of Python3 online submissions for Add Strings.
Memory Usage: 14 MB, less than 92.72% of Python3 online submissions for Add Strings.
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def to_digit(num):
            res = 0
            for k in range(len(num)-1,-1,-1):   # 2,1,0
                power = len(num) - 1 - k
                res += int(num[k])*(10**power)
            return res
        return str(to_digit(num1) + to_digit(num2))


def test_solution():
    inp = [ ("11", "123"),
            ("456", "77"),
            ("0", "0")
          ]
    out = ["134", "533",  "0"]
    # inp = [("11", "123")]
    # out = ["134"]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.addStrings(inp[i][0], inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()




if __name__ == '__main__':
    test_solution()

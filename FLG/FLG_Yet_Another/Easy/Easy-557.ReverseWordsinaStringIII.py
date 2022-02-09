"""
557. Reverse Words in a String III (Easy)

Main Idea. Stack
1) For all symbols c in the string
    2) Push all the symbols c into stack
    3) If c == " "
         pop all from the stack and add into string

Time complexity: O(N)
for loop O(n)
pop all symbols from stack O(N)

Space complexity: O(N)
create new string O(N)

Runtime: 161 ms, faster than 6.77% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.7 MB, less than 81.32% of Python3 online submissions for Reverse Words in a String III.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        aux = ''
        stack = []
        n = len(s) - 1
        for k, v in enumerate(s):
            if v == " ":  # End of world. pop all from stack
                while stack:
                    aux += stack.pop()
                aux += v
            elif k == n:
                aux += v
                while stack:
                    aux += stack.pop()
            else:
                stack.append(v)
        return aux


def test_solution():
    inp = [ "Let's take LeetCode contest",
            "God Ding",
            "a",
          ]
    out = ["s'teL ekat edoCteeL tsetnoc",
           "doG gniD",
           "a"]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.reverseWords(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()

"""
125. Valid Palindrome (Easy)

Main Idea:
Two pointers

Time complexity: O(N)

Space complexity: O(1)

Runtime: 71 ms
Memory Usage: 14.5 MB

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return False
        lo = 0
        hi = len(s)-1

        while lo <= hi:

            if s[lo].upper() != s[hi].upper():
                if not s[hi].upper().isalnum():
                    hi -= 1
                elif not s[lo].upper().isalnum():
                    lo += 1
                else:
                    return False
            else:
                lo += 1
                hi -= 1
        return True


def test_solution():
    inp = ["A man, a plan, a canal: Panama",
           "race a car",
           " ",
          ]
    out = [True, False, True]

    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.isPalindrome(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
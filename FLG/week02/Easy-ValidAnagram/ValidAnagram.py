"""
Runtime: 60 ms, faster than 23.79% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.6 MB, less than 45.86% of Python3 online submissions for Valid Anagram.

Time complexity: O(N)
Space compexity: O(N+M)

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        alphabet_s = {}
        alphabet_t = {}

        for l in s:                             # O(N)
            if l in alphabet_s.keys():
                alphabet_s[l] += 1
            else:
                alphabet_s[l] = 1

        for l in t:                             # O(N)
            if l in alphabet_t.keys():
                alphabet_t[l] += 1
            else:
                alphabet_t[l] = 1

        for key in alphabet_s.keys():           # O(M), M = 26
            if key not in alphabet_t.keys():
                return False
            elif alphabet_s[key] != alphabet_t[key]:
                return False

        return True


def test_isAnagram():
    inp = [["anagram","nagaram"],
           ["rat","car"]]
    out = [True, False]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.isAnagram(inp[i][0],inp[i][1])
        print()
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")


if __name__ == '__main__':
    test_isAnagram()











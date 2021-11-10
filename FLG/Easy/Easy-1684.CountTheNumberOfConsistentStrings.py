"""
(Easy) 1684.Count the Number of Consistent Strings

Main Idea:

Time complexity: O(n*m)

Space complexity: O(n+m) + plus extra space for diffs

Runtime: 300 ms, faster than 34.79% of Python3 online submissions for Count the Number of Consistent Strings.
Memory Usage: 17.5 MB, less than 5.58% of Python3 online submissions for Count the Number of Consistent Strings.

"""


class Solution:
    def countConsistentStrings(self, allowed, words):
        count = 0
        diffs = [set(word) - set(allowed) for word in words]
        for diff in diffs:
            if not diff:
                count +=1

        return count

def test_solution():
    inp = [("ab",["ad","bd","aaab","baa","badab"]),
           ("abc",["a","b","c","ab","ac","bc","abc"]),
           ("cad", ["cc","acd","b","ba","bac","bad","ac","d"])
          ]
    out = [2,7,4]
    sol = Solution()

    for i in range(len(inp)):
        test_rest = sol.countConsistentStrings(inp[i][0], inp[i][1])
        print('test_rest', test_rest)
        print("Test", i + 1, ":", "OK\n" if test_rest == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
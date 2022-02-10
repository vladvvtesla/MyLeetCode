"""
443. String Compression (Medium)

Main Idea.
Two pointers

Time complexity: O(N)

Space complexity: O(1)
Runtime: 113 ms, faster than 12.95% of Python3 online submissions for String Compression.
Memory Usage: 13.9 MB, less than 94.90% of Python3 online submissions for String Compression.
"""
class Solution:
    def compress(self, chars) -> tuple:
        n = len(chars)

        if n <= 1:
            return (n, chars)   #   retun n for Leetcode

        r, w = 0, 0

        while r < n:
            count = 1
            while r < n - 1 and chars[r] == chars[r + 1]:
                count += 1
                r += 1

            chars[w] = chars[r]
            w += 1
            if count != 1:
                for d in str(count):
                    chars[w] = d
                    w += 1
            r += 1

        return (w, chars[:w])    # return w for Leetcode


def test_solution():
    inp = [ ["a","a","b","b","c","c","c"],
            ["a"],
            ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
            ['a', 'b', 'b', 'a', 'a'],
            ["a", "b", "c"]
            ]
    out = [(6, ["a","2","b","2","c","3"]),
           (1, ["a"]),
           (4, ["a","b","1","2"]),
           (5, ['a', 'b', '2', 'a', '2']),
           (3, ["a","b","c"])
           ]
    # inp = [['a', 'b', 'b', 'a', 'a']]
    # out = [(5, ['a', 'b', '2', 'a', '2'])]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.compress(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()

"""
1143. Medium - Longest Common Subsequence

Main Idea: DP
Explonation:
https://www.youtube.com/watch?v=ASoaQq66foQ&list=PLiQ766zSC5jM2OKVr8sooOuGgZkvnOCTI&index=3

Time complexity: O(MxN)

Space complexity: O(MxN)

Runtime: 396 ms, faster than 81.25% of Python3 online submissions for Longest Common Subsequence.
Memory Usage: 21.9 MB, less than 88.68% of Python3 online submissions for Longest Common Subsequence.
"""
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        if text1 == text2 == 0: return 0       # edge case

        m = len(text1)+2       # row_index    0 - "" empty substring
        n = len(text2)+2       # col_index    0 - "" empty substring
        auxArr = [[0] * m] * n

        # Fill the first row
        auxArr[0] = ["", ""] + list(text1)

        # Fill the first col
        col0 = ["", ""] + list(text2)
        for k in range(n):
            auxArr[k] = auxArr[k][:]
            auxArr[k][0] = col0[k]

        # for row in auxArr:
        #     print(row)
        # ['', '', 'a', 'b', 'c', 'd', 'e']
        # ['',  0,  0,   0,   0,   0,   0]
        # ['a', 0,  0,   0,   0,   0,   0]
        # ['c', 0,  0,   0,   0,   0,   0]
        # ['e', 0,  0,   0,   0,   0,   0]

        for k in range(2,n):               # rows
            for j in range(2, m):          # cols
                # print('k','j',':', k, j)
                # print(auxArr[k][0])          # Text1[0] row
                # print(auxArr[0][j])          # text2[0] col
                if auxArr[k][0] == auxArr[0][j]:
                    auxArr[k][j] = 1 + auxArr[k-1][j-1]
                else:
                    auxArr[k][j] = max(auxArr[k-1][j], auxArr[k][j-1])

        # print()
        # for row in auxArr:
        #     print(row)
        # ['', '', 'a', 'b', 'c', 'd', 'e']
        # ['',  0,  0,   0,   0,   0,   0]
        # ['a', 0,  1,   1,   1,   1,   1]
        # ['c', 0,  1,   1,   2,   2,   2]
        # ['e', 0,  1,   1,   2,   2,   3]

        return auxArr[n-1][m-1]

def test_longestCommonSubsequence():

    inp = [("abcde","ace"), ("abc","abc"), ("abc", "def"), ("", ""), ("a", "ab"),
           ("ab", "a"), ("", "ab"), ("bsbininm","jmjkbkjkv"), ("aa", "a")]
    out = [3, 3, 0, 0, 1, 1, 0, 1, 1]

    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.longestCommonSubsequence(inp[i][0],inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_longestCommonSubsequence()
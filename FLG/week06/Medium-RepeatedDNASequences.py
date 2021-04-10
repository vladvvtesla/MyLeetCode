"""
187. Repeated DNA Sequences

Main Idea
1) For all 10-letter-long sequences add new key into dictionary
2) return all keys from dictionary if value > 1

Time complexity:

Space complecity:     O( (N-L)*L )
For each N-10 symbols in s:     O(N-10)
     make 10-symbols-slice:     O(10)
     add key into dict:         const
     or increment value:        const
Geneate result List from dict:  O(M)  M<N

Runtime: 64 ms, faster than 67.59% of Python3 online submissions for Repeated DNA Sequences.
Memory Usage: 27.8 MB, less than 22.98% of Python3 online submissions for Repeated DNA Sequences.
"""
class Solution:
    def findRepeatedDnaSequences(self, s):
        # For all 10-letter-long sequences add new key into dictionary
        # return all keys from dictionary if value > 1
        if len(s) < 10:
             return []

        d ={}
        for k in range(len(s)-9):
            if s[k:k+10] in d.keys():
                d[s[k:k+10]] += 1
            else:
                d[s[k:k+10]] = 1

        return [key for key, value in d.items() if value > 1]


def test_findRepeatedDnaSequences():
    inp = ["AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
           "AAAAAAAAAAAAA",
           "AAAAAAAAAAA"]
    out = [["AAAAACCCCC","CCCCCAAAAA"],
           ["AAAAAAAAAA"],
           ["AAAAAAAAAA"]]

    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.findRepeatedDnaSequences(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_findRepeatedDnaSequences()
"""
443. String Compression (Medium)

Main Idea.
1) Пройтись по всему chars и сосчитать число вхождений символом
   и на основе собранной информации создать новый  aux

Time complexity: O(N)

Space complexity: extra space O(n) for aux

Runtime: 124 ms, faster than 6.03% of Python3 online submissions for String Compression.
Memory Usage: 14.1 MB, less than 85.54% of Python3 online submissions for String Compression.
"""
class Solution:
    def compress(self, chars) -> tuple:
        def _count_digits(count):
            res = []
            while count:
                res.append(count % 10)
                count //= 10
            res.reverse()
            return [str(x) for x in res]

        if len(chars) == 1: return (1, chars)  # Edge case # return 1  For leetcode
        aux = []
        n = len(chars) - 1
        count = 1

        for k, v in enumerate(chars):
            if k == 0: continue
            if v == chars[k-1]:
                count += 1
                if k == n:  # Handle the end of chars
                    aux.append(v)
                    aux.extend(_count_digits(count))
            elif v != chars[k-1]:
                aux.append(chars[k-1])
                if count > 1:
                    aux.extend(_count_digits(count))
                count = 1
                if k == n:  # Handle the end of chars
                    aux.append(v)



        # modify the input arr
        for k, v in enumerate(aux):
            chars[k] = v

        # return len(aux)  # For leetcode
        return (len(aux), chars[:len(aux)])


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

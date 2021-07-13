"""
22. Medium Generate Parentheses

Main Idea:
                       genPar('', 3, 3)                   # One choise
                         /
                    genPar('(' 2, 3)                     # Two choises
                     /               \
            genPar('()' 2, 2)      genPar('((' 1, 3)
                /                    /             \
        genPar('()('1, 2)     genPar('(((' 0, 3)   genPar('(()' 1, 2)

        # if len('((()))') == n:                        #   base case, stop recursion

Time complexity: O(n)

Space complexity: O(n)

Runtime: 36 ms, faster than 64.10% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.7 MB, less than 38.82% of Python3 online submissions for Generate Parentheses.
"""
class Solution:
    def generateParenthesis(self, n):

        def _genPar(p, l, r, aux, n):
            if len(p) == 2 * n:   # Если строка заполнена, добавить ее в список решений
                aux.append(p)
                return p
            elif l == 0 and r != 0:          # только зыкрыть, иначе некорректная послед-ть
                return _genPar(p + ')', l, r-1, aux, n)
            elif r == 0 and l != 0:          # только открыть, иначе некорректная послед-ть
                return _genPar(p + '(', l - 1, r, aux, n)
            elif l == r:                    # только открыть, иначе некорректная послед-ть
                return _genPar(p + '(', l - 1, r, aux, n)
            else:                            #  l > r,  l < r
                return _genPar(p + '(', l - 1, r, aux, n) and _genPar(p + ')', l, r - 1, aux, n)

        if n == 0: return []     # edge case
        aux = []
        p = ''
        l = n   # Number of left Parenthesis
        r = n   # Number of right Parenthesis

        _genPar(p, l, r, aux, n)

        return aux

def test_solution():
    inp = [0, 1, 2, 3]
    out = [[],
           ["()"],
           ['(())', '()()'],
           ['()(())', '(()())', '()()()', '((()))', '(())()'],
           ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"],
           ["((((()))))", "(((()())))", "(((())()))", "(((()))())", "(((())))()", "((()(())))", "((()()()))", "((()())())", "((()()))()", "((())(()))", "((())()())", "((())())()", "((()))(())", "((()))()()", "(()((())))", "(()(()()))", "(()(())())", "(()(()))()", "(()()(()))", "(()()()())", "(()()())()", "(()())(())", "(()())()()", "(())((()))", "(())(()())", "(())(())()", "(())()(())", "(())()()()", "()(((())))", "()((()()))", "()((())())", "()((()))()", "()(()(()))", "()(()()())", "()(()())()", "()(())(())", "()(())()()", "()()((()))", "()()(()())", "()()(())()", "()()()(())", "()()()()()"]
           ]
    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.generateParenthesis(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_solution()
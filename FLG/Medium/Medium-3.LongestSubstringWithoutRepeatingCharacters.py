"""
3. Longest Substring Without Repeating Characters

Main Idea
Two pointers
1) Бежать по строке
2)   Для каждого символа  еще раз пробежать по строке от lo до символа
  3) Если ранее не было такого же символа, то  lo остается равным 0
  4) если же символ уже был, то lo сдвигаем на тот индекс, где уже был этот символ
     И при этом для res выбираем максимальное значение из двух
     res =  res = max(res, k+1 - lo)

Time complexity: O(n^2)
1) пробежаться по всей строке: O(n)
2) пробежаться от lo до k, чтобы проверить, не встречали ли ранее этот символ:
   в худшем случае, когда lo совсем не сдвигается, O(1) + O(2)+ O(n) = O(n/2)

Space complexity: O(n)
No extra space


Runtime: 117 ms, faster than 28.41% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.5 MB, less than 24.95% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)                    # Two edge cases

        res = 0
        lo = 0
        for k,val in enumerate(s):
            for j in range(lo, k):
                if val == s[j]:              # find not unique symbol
                    lo = j + 1
                    break
            res = max(res, k+1 - lo)
        return res



def test_lengthOfLongestSubstring():

    inp = ["abcabcbb", "bbbbb", "pwwkew", "", " ", "au", "aab", "dvdf", "fdvdz"]
    out = [3, 1, 3, 0, 1, 2, 2, 3, 3]

    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.lengthOfLongestSubstring(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_lengthOfLongestSubstring()
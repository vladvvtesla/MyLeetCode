"""
387. First Unique Character in a String (Easy)

Main Idea.
1) Создать вспомогательный set notuniq:
2) res = -1
3) двигаем k направо
     res устанавливаем на k (кандидат на решение)
     если s[K] есть в notuniq:
         res сбрасываем на -1 и двигаемся дальше
     если s[k] нет в notuniq:
         проверить, есть ли s[k] в оставшейся полдстроке
            если есть:
            s[k] добавляем в список неуникальных
            res сбрасываем на -1
            если не:
            нашли уникальный элемент, вернуть k
     когда дошли до конца возвращаем res

Time complexity: O(n^2)
Space complexity: O(n)

Runtime: 55 ms, faster than 99.40% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.1 MB, less than 96.56% of Python3 online submissions for First Unique Character in a String.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        notuniq = set()

        for k in range(len(s)):
            if s[k] in notuniq:
                continue
            if s[k] in s[k+1:]:
                notuniq.add(s[k])
            else:
                return k

        return -1


def test_solution():
    inp = [ "leetcode", "loveleetcode", "aabb", "", "a", "aa", "aabbc",
          ]
    out = [0, 2, -1, -1, 0, -1, 4]
    # inp = ["aabb"]
    # out = [-1]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.firstUniqChar(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")
        print()




if __name__ == '__main__':
    test_solution()

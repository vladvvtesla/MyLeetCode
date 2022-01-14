"""
739 Daily Temperatures (Medium)


Main Idea: Using Stack

1) Бежим по всему списку temperatures
2) Если текущая температура больше предыдущей,
   то проверяем стэк , и пока стэк у нас заполнен, делаем следующее:
   в ответы в предыдущий день записываем 1, но не просто один а разницу интексов 6-5 =1
   Если стэк все еще не пуст, то в ответ пред-предыдущего дня записываем 6-4 = 2

   Если стэк все еще полон, но при этом температура[6] меньше температуры[3],
   то не записываем ответ[3], а прерываем цикл while
   и в любом случае текущий индекс записываем в стэк
3) Если же текущая температура меньше или равна предыдущей,
   просто добавляем индекс текущей температуры в стэк

TimeComplexity: O(n)
O(n) чтобы пройтись по списку temperatures
Стэк в худшем случае расзрастается до O(n),
но из него в сумме нужно вытащить эти же N значений,
поэтому плюс O(n)
2 * O(n) -> O(n)

Space Complexity: O(n) plus extra space O(n) for stack

Runtime: 1464 ms, faster than 28.06% of Python3 online submissions for Daily Temperatures.
Memory Usage: 24.9 MB, less than 84.91% of Python3 online submissions for Daily Temperatures.
"""


class Solution:
    def dailyTemperatures(self, temperatures):
        answers = [0]*(len(temperatures))
        stack = []
        for k,val in enumerate(temperatures):
            if val > temperatures[k-1]:
                while stack and val > temperatures[stack[-1]]:
                    idx = stack.pop()
                    answers[idx] = k - idx     # answer[5] = 6-5 = 1
            stack.append(k)

        return answers


def test_solution():
        inp = [[73,74,75,71,69,72,76,73],
               [30, 40, 50, 60],
               [30, 60, 90],
               [79, 78, 77, 76, 75, 74, 73, 72],
               [73],
               []
               ]
        out = [[1,1,4,2,1,1,0,0],
               [1, 1, 1, 0],
               [1, 1, 0],
               [0,0,0,0,0,0,0,0],
               [0],
               []
               ]
        sol = Solution()
        for i in range(len(inp)):
            test_res = sol.dailyTemperatures(inp[i])
            print()
            print('test_res', test_res)
            print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")

if __name__ == '__main__':
    test_solution()
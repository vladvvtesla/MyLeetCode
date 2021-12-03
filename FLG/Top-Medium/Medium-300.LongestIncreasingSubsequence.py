"""
300. Longest Increasing Subsequence  (Top-Medium) - Dyn Prog

Main Idea:
Долго бился над этой задачей, в итоге обратился к разбору решения на youtube-канале
https://www.youtube.com/watch?v=fV-TF4OvZpk&list=PLiQ766zSC5jM2OKVr8sooOuGgZkvnOCTI&index=18

[10,9,2,5,3,7,101,18]

Указатели i и j показывают на границы подмассива для которого ищем решение.
Сначала  j двигаем вправо, затем i

В aux запысываем везде 1, так как по умолчанию для каждого подмассива у нас решение 1
В aux[0] записываем ответ для подмассива nums[0:1] = [10], в aux[1] - решение для  nums[0:2] = [10,9]
Затем указатель j перемещаем вправо и проверяем
добавление этого элемента nums[1] улучшает ли решение для каждого рассмотренного ранее подмассива,
для [10] - не улучшает,
поэтому решение для [10,9] тоже будет 1 и записываем его в

Для случая [10,9,2,5]
изначально aux = [1, 1, 1, 1]
i = 0
j = 3
проверяем для nums[:1] = [10] - добавление 5 не улучшает решение, поэтому aux[3] = 1
проверяем для nums[:2] = [10,9]- добавление 5 не улучшает решение, поэтому aux[3] = 1
проверяем для nums[:3] = [10,9,2]- добавление 5  улучшает решение!, поэтому
 к найденному ранее решению aux[2] = 1 прибавляем 1 и записываем в aux[3]
 таким образом aux = [1, 1, 1, 2]
 Важно! записываем новое значение в aux[3], только если нашли лучшее решение

Далее таким же образом заполняем aux. Возвращаем максимальное значение из aux


Time complexity: O(n^2)

Space complexity: O(n) plus O(n) extra space for aux

Runtime: 3992 ms, faster than 31.49% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14.7 MB, less than 17.43% of Python3 online submissions for Longest Increasing Subsequence.

"""
class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0: return 0       # Edge case

        j = 0
        aux = [1] * len(nums)

        for j in range(len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    aux[j] = max(aux[j], aux[i] + 1)   #  Важно! записываем, только если нашли лучшее решение

        return max(aux)


def test_solution():
    inp = [[10,9,2,5,3,7,101,18],
           [0, 1, 0, 3, 2, 3],
           [7, 7, 7, 7, 7, 7, 7],
           [],
           [4, 10, 4, 3, 8, 9]
          ]
    # inp = [[0, 1, 0, 3, 2, 3]]
    out = [4,4,1, 0, 3]
    # out = [4]
    sol = Solution()

    for i in range(len(inp)):
        test_rest = sol.lengthOfLIS(inp[i])
        print('test_rest', test_rest)
        print("Test", i + 1, ":", "OK\n" if test_rest == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
"""
922. Sort Array By Parity II (Easy)

Main Idea:
Бежим двумя указателями по nums.
1) если встретили элемент, который стоит не на своем месте, (например, четный)
    2) второй индекс бежит вперед, пока не встретит подходящий элемент (нечетный)
    3) когда нашли, то меняем местами эдементы первого и второго индекса.
4) завершить цикл, когда дошли до конца nums


Time complexity:
пробежаться по всему nums: O(n) O(n^2)
найти подхоодящий элемент в половине случаев
и найдется он в среднем не в конце, в ближе: 1/2 * O(1/2 * n) = 1/4 O(n)
Итого 1/4 O(n^2) = O(n^2)

Space Complexity: in place

Runtime: 344 ms, faster than 14.49% of Python3 online submissions for Sort Array By Parity II.
Memory Usage: 16.3 MB, less than 71.63% of Python3 online submissions for Sort Array By Parity II.

"""
class Solution:
    def sortArrayByParityII(self, nums):
        for i in range(len(nums)):
            if i % 2 == 0 and nums[i] % 2 != 0:
                for j in range(i+1, len(nums)):
                    if j % 2 != 0 and nums[j] % 2 == 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break

            elif i % 2 != 0 and nums[i] % 2 == 0:
                for j in range(i+1, len(nums)):
                    if j % 2 == 0 and nums[j] % 2 != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break

        return nums


def test_solution():
    inp = [[5,1,2,3,4,0], [4,2,5,7],[2,3],
           ]
    # inp = [([5,7,7,8,8,10,12],12)]
    out = [[0,1,2,3,4,5],[4,5,2,7],[2,3],]
    # out = [[6,6]]

    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.sortArrayByParityII(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")

if __name__ == '__main__':
    test_solution()
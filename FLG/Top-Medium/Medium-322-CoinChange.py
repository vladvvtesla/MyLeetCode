"""
322. Medium - Coin Change

0. Задача похожа на "Задачу о кузнечике" и решается динамическим программированием
1. Из coins убрать все coin > amount, так как когда даем сдачи 1 руб,
        нам не нужны 2, 5, 10 руб.  Это покроет ряд edge case
2. Построить вспомогательный массив длины [max(coin) + amount + max(coin) + 1]
   Заполненный сразу значениями -1. То есть по-умолчанию все сзначения amount недостижимы
   И нуль-пункт у нас будет не aux[0], а aux[zero_point] и zero_point = mac(coins)
3. При amount = 0 мы знаем, что нам для сдачи монеты не нужны,
   то есть мы знаем это значение без вычислений и заполняем его  aux[zero_point] = 0
4. Далее из точки 0 мы можем допрыгнуть за самую короткую траекторию в 1 прыжок до
   значений 1, 2, 5.
   Поэтому эти значения нам известнв и сразу заполняем aux[zero_point+1] = 1, aux[zero_point+2] = 2
5. Далее наша цель посчитать, как мы можем допрыгать от 0 до 11, когда у нас прыжки длиной
   в 1, 2 и 5
   то есть начинаем заполянть все aux[zero_point + 0] ... aux[zero_point + 11],
   если они еще не заполнены.
6. Если до 2 есть несколько траекторий:
   от 0 до 2 один прыжок длиной 2
   от 1 до 2 один прыжок длиной 1
   от -3 до 2 один прыжок длиной 5, то выбираем минимальную из доступных,
   но так как на поле -3 у нас значение -1, то такая траектория невозможна и
   получаем     min([1,1]) = 1 тогда    aux[zero_point + 2] = 1
7. Если мы не можем допрыгать до 11, то оно остается по-умолчанию -1
8. Такми образом считаем, пока не дойдем до aux[zero_point + 11]
9. Возвращаем aux[zero_point + 11]


Time complexity: O(N)
1) Из coins убрать все coin > amount : O(amount)
2) заполнить известные значения (O(len(coins))) + 1 = O(amount)
3) Заполнить все остальные значения от 0 до amount = O(amount)

Space complexity: O(3*amount)
1) O(2*max(coins) + amount) = O(2*amount + amount) = O(3*amount)


Runtime: 1300 ms, faster than 76.42% of Python3 online submissions for Coin Change.
Memory Usage: 14.6 MB, less than 47.56% of Python3 online submissions for Coin Change.
"""
class Solution:
    def coinChange(self, coins, amount):
        if amount == 0: return 0                 # edge case

        # edge case - erase all coin > amount
        coins = [coin for coin in coins if coin <= amount]
        if not coins: return -1

        zero_point = max(coins)                  # We need negative indexes aux[-5] == -1
        aux = [-1] * (zero_point + amount + zero_point + 1)   # Init auxilary list
        aux[zero_point] = 0                      # For amount 0 we have 0 traectories

        for coin in coins:
            aux[zero_point+coin] = 1             # For amount 1 or 2 or 5 we have 1 shortest traectory

        # Начинаем высчитывать траектории для всех amount от 1 до 11
        for k in range(zero_point+1, amount + zero_point + 1):
            if aux[k] < 0:          # считаем только для тех, для кого еще не считали

                # до 6 мы можем допрыгать 3 способами
                # из 5 прибавив 1,
                # из 4 прибавив 2
                # из 1 прибавив 5
                # то есть траектория до 6, это у нас самая короткая траектория до 4,
                # плюс один прыжок. А самая короткая траектория до 4 была посчитана ранее
                traectories = [aux[k-coin]+1 for coin in coins]

                # Из траекторий убираем все 0, так как это озгачает,
                # что мы попробовали из недоступной траектории (-1) сделать 1 прыжок (+1)
                # и получили 0. Хотя на самом деле мы снова оказались на недоступной
                # траектории. Поэтому убираем длину 0 и выбираем меньшее из оставшихся
                traectories = [i for i in traectories if i != 0]

                if traectories:
                    aux[k] = min(traectories)
                else:
                    aux[k] = -1   # если нет ни одной траектории, то записываем -1

        return aux[zero_point+amount]         # For 11 we should return aux[11+5]


def test_coinChange():
    inp = [ ([1,2,5], 11), ([2], 3), ([1], 0), ([1], 1), ([1], 2), ([2], 1),
            ([2147483647],2), ([1,2147483647],2)]
    out = [3,-1,0, 1, 2, -1, -1, 2]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.coinChange(inp[i][0], inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()


if __name__ == '__main__':
    test_coinChange()

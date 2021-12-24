"""
380. Insert Delete GetRandom O(1)   (Top Medium)

Main Idea: Dict and random.choise()

Time complexity:

Space Conplexity: O(n)

Runtime: 784 ms, faster than 15.89% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 61.4 MB, less than 96.32% of Python3 online submissions for Insert Delete GetRandom O(1).

"""


class RandomizedSet:

    def __init__(self):
        self.d = dict()

    def insert(self, val):
        if val in self.d.keys():          # O(?)
            return False
        else:
            self.d[val] = 1               # O(1)
            return True

    def remove(self, val):
        item = self.d.pop(val, None)      # O(?)
        return True if item else False

    def getRandom(self):
        import random
        return random.choice(list(self.d.keys()))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

obj = RandomizedSet()
param_1 = obj.insert(5)
param_2 = obj.insert(6)
param_3 = obj.remove(5)
param_4 = obj.getRandom()
print([None, param_1, param_2, param_3, param_4])
print('[None, True, True, True, 6] Should be\n ')
print()


obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.insert(2)
param_4 = obj.getRandom()
param_5 = obj.remove(1)
param_6 = obj.insert(2)
param_7 = obj.getRandom()
print([None, param_1, param_2, param_3, param_4, param_5, param_6, param_7])
print('[None, True, False, True, 2, True, False, 2] Should be\n  ')
print()






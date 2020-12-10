# 28 ms # 14.4 MB
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        """leetcode #771"""
        count = 0
        jdict = {j: 0 for j in J} # dict of zeros for jews
        for s in S:
            if s in jdict.keys():
                count += 1

        return count


# TESTS
def test_jewels_and_srones1():
    j = "aA"
    s = "aAAbbbb"
    res = 3
    sol = Solution()
    test_res = sol.numJewelsInStones(j, s)
    print("Test1: ", "OK" if test_res == res else "Failed")


def test_jewels_and_srones2():
    j = "z"
    s = "ZZ"
    res = 0
    sol = Solution()
    test_res = sol.numJewelsInStones(j, s)
    print("Test2: ", "OK" if test_res==res else "Failed")

test_jewels_and_srones1()
test_jewels_and_srones2()

if __name__ == '__main__':
    j = "aA"
    s = "aAAbbbb"
    sol = Solution()
    print(sol.numJewelsInStones(j, s))
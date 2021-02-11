class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:




def test_countConsistentStrings():
    alloweds = ["ab",
                "abc",
                "cad"]
    words_lists =  [["ad","bd","aaab","baa","badab"],
                   ["a","b","c","ab","ac","bc","abc"],
                   ["cc","acd","b","ba","bac","bad","ac","d"]]
    out = [2,7,4]
    sol = Solution()
    for i in range(len(alloweds)):
        test_res = sol.countConsistentStrings(alloweds[i], words_lists[i])
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")

if __name__ == '__main__':
    test_countConsistentStrings()
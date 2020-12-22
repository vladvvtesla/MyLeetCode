
#Runtime: 32 ms, faster than 37.03% of Python3
# Memory Usage: 14 MB, less than 81.98% of Python3
class Solution:
    def toLowerCase(self, some_string: str) -> str:
        """
        Make a dict of characters {'A': 'a', ...}
        for c in string
           if c in dict.keys()
               put dict[c] instead c
        """
        result = list(some_string)
        abc = {'A': 'a', 'B': 'b',  'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f',
               'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l',
               'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r',
               'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x',
               'Y': 'y', 'Z': 'z',
               }
        for k in range(len(result)):
            if result[k] in abc.keys():
                result[k] = abc[result[k]]
        return "".join(result)

def test_toLowerCase():
        inp = ["Hello", "here", "LOVELY"]
        out = ["hello", "here", "lovely"]
        sol = Solution()
        for i in range(len(inp)):
            test_res = sol.toLowerCase(inp[i])
            print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")

if __name__ == '__main__':
    test_toLowerCase()
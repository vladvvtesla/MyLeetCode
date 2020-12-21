### 1108. Defanging an IP Address

# Runtime: 28 ms, faster than 73.22% of Python3
# Memory Usage: 14.3 MB, less than 18.55% of Python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Using Split and join
        sa = address.split('.')
        result = "[.]".join(sa)
        return result


# Runtime: 32 ms, faster than 40.43% of Python3
# Memory Usage: 14.3 MB, less than 18.55% of Python3
class Solution1:
    def defangIPaddr(self, address: str) -> str:
        # make empty string
        # For each character in ip_address_string
        # if character!="." join character else join "[.]"
        # return result string
        result = ""

        for char in address:
            if char != ".":
                result += char
            else:
                result += "[.]"

        return result


def test_defanging_address():
    inp = ["1.1.1.1", "255.100.50.0"]
    out = "1[.]1[.]1[.]1", "255[.]100[.]50[.]0"
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.defangIPaddr(inp[i])
        print("Test", i+1, ":", "OK" if test_res == out[i] else "Failed")

if __name__ == '__main__':
    test_defanging_address()
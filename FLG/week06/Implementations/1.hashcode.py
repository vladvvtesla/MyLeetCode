def hashCode(string):
    """Horners method to hash string of length L
       hashCode("call") = 3045982
       string: some string
       return hash:  integer
    """
    hash = 0
    for s in string:
        hash = ord(s) + 31 * hash
    return hash

def test_hashCode():
    inp = ["call", "test"]
    out = [3045982, 3556498]
    for i in range(len(inp)):
        test_res = hashCode(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()

if __name__ == '__main__':
    test_hashCode()
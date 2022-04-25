"""
535. Encode and Decode TinyURL (Medium)

Runtime: 40 ms, faster than 71.60% of Python3 online submissions for Encode and Decode TinyURL.
Memory Usage: 14 MB, less than 28.27% of Python3 online submissions for Encode and Decode TinyURL.
"""

class Codec:
    def __init__(self):
        self.hash_db = {}
        self.url_db = {}
        self.base_url = 'http://tinyurl.com/'
        self.salt = 'fngkdt'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.url_db.keys():
            return self.base_url + self.url_db[longUrl]

        new_str = longUrl + self.salt
        hashsum = 0
        for c in new_str:
            hashsum += ord(c)
        res = self.base_url + str(hashsum)
        self.hash_db[str(hashsum)] = longUrl
        self.url_db[longUrl] = str(hashsum)

        return res

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        hash_str = shortUrl[19:]
        return self.hash_db[hash_str]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

if __name__ == '__main__':
    inp = ["https://leetcode.com/problems/design-tinyurl", ]
    out = ["https://leetcode.com/problems/design-tinyurl", ]

    for i in range(len(inp)):
        codec = Codec()
        test_res = codec.decode(codec.encode(inp[i]))
        print('test_res', test_res)
        print('OK\n') if test_res == out[i] else print('False\n')
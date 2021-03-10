"""
Regions Cut By Slashes (Medium)



Runtime: 120 ms, faster than 90.14% of Python3 online submissions for Regions Cut By Slashes.
Memory Usage: 14.6 MB, less than 88.99% of Python3 online submissions for Regions Cut By Slashes.

"""

class UnionFind():
    """" Weighted  QuickUnion with Path Compression.  Coursera Sedgewick 1 w1"""
    def __init__(self, n):
        """ self.id is an array of integer
            self.id[i] is parent of i
            root of i is id[id[...id[i]...]]   # keep going until it doesn't change
        """
        self._count = n                     # number of components
        self.id = [i for i in range(n)]     # the constructor: set id of each object to itself
        self.sz = [1,] * n                  # maintain extra array to count number of objects
                                            # in the tree rooted at i

    def root(self, i):
        """ root of i is id[id[...id[i]...]]   # keep going until it doesn't change """
        while i != self.id[i]:
            # Make every other node in path point to its grandparent
            # (there by halving path length)
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def count(self):
        """Return the number of componets."""
        return self._count

    def connected(self, p, q):
        """Check if the items p and q have the same root or not."""
        return self.root(p) == self.root(q)

    def union(self, p, q):
        """ To merge components containing p and q set the id of p's to the id of q's root
            1) Link root of smaller tree to root of larger tree
            2) update the sz array
        """
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        self._count -= 1                # decrease number of components, if union different roots
        if self.sz[i] < self.sz[j]:
            self.id[i] = j              # change root of p
            self.sz[j] += self.sz[i]    # update size of the tree
        else:
            self.id[j] = i              # change root of q
            self.sz[i] += self.sz[j]

    def __str__(self):
        print('i: ', 'id[i]')
        for i in range(len(self.id)):
            print(i, ':', self.id[i])
        return '\n'


class Solution:
    def regionsBySlashes(self, grid) -> int:
        n = len(grid)
        # Initialise UF Data Structure
        uf = UnionFind(2 * (n**2 + n))

        # Call union method for connected areas
        for j in range(n):
            for k in range(n):
                if grid[j][k] == '/':
                    p = j*n + k                   # 3
                    q = (n**2 + n) + k*n + j      # 9
                    uf.union(p,q)
                    p = (n**2 + n) + (k+1)*n + j  # 11
                    q = (j+1)*n + k               # 5
                    uf.union(p,q)
                elif grid[j][k] == '\\':
                    p = j*n + k                   # 3
                    q = (n**2 + n) + (k+1)*n + j  # 11
                    uf.union(p,q)
                    p = (n**2 + n) + k*n + j      # 9
                    q = (j+1)*n + k               # 5
                    uf.union(p,q)
                else:
                    p = j*n + k                   # 3
                    q = (n**2 + n) + (k+1)*n + j  # 11
                    uf.union(p,q)
                    p = j*n + k                   # 3
                    q = (n**2 + n) + k*n + j      # 9
                    uf.union(p,q)
                    p = j*n + k                   # 3
                    q = (j+1)*n + k               # 5
                    uf.union(p,q)

        return uf.count()


def test_regionsBySlashes():
    inp = [
         [ " /", "/ " ],
         [ " /", "  " ],
         ["\\/", "/\\"],
         ["/\\", "\\/"],
         ["//", "/ "]
         ]
    out = [2, 1, 4, 5, 3]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.regionsBySlashes(inp[i])
        print()
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")

if __name__ == '__main__':
    test_regionsBySlashes()
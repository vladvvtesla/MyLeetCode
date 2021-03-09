"""
Number of provinces (Medium)

Runtime: 204 ms, faster than 43.35% of Python3 online submissions for Number of Provinces.
Memory Usage: 14.5 MB, less than 96.89% of Python3 online submissions for Number of Provinces.
"""

"""
Union command:  connect two objects
Find/connected query: is there a path connecting the two objects
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
        i =  self.root(p)
        j =  self.root(q)
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
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        # Initialise UF Data Structure
        uf = UnionFind(n)

        # Call union method for connected cities
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i,j)

        # number of unuiques provinces is equal to number of roots
        return uf.count()


def test_findCircleNum():
    inp = [
          [[1,1,0],[1,1,0],[0,0,1]],
          [[1,0,0],[0,1,0],[0,0,1]]
          ]
    out = [2, 3]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.findCircleNum(inp[i])
        print()
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")

if __name__ == '__main__':
    test_findCircleNum()

"""

    # n = len(isConnected[1])
    n = 10
    print('n: ', n)
    # Initialise UF Data Structure
    uf = WQUPC(n)

    print(uf.root(1))

    uf.union(3,4)
    uf.union(3,8)
    uf.union(6,5)
    uf.union(9,4)
    uf.union(2,1)
    uf.union(5,0)
    uf.union(7,2)
    uf.union(6,1)
    uf.union(7,3)
    print(uf)
    print(uf.connected(2,1))
    print(uf.connected(5,4))

    # Call root method and count number of unique roots
    s = set()
    for i in range(n):
        root = uf.root(i)
        print("root", root)
        s.add(root)
    print(len(s))

"""
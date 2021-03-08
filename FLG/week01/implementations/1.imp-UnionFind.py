"""

Data structure: an array of integers
                and an extra array for sizes of trees
Union command:  connect two objects
Find/connected query: is there a path connecting the two objects

Connected components - maximal set of objects, that are mutually connected

Find query: Check if two objects are in the same component.
Union: To merge components containing p and q set the id of p's to the id of q's root


UF class methods
union()
connected()
find() component identifier for p (from 0 to M-1)
count() number of components

Improvement 1: Weighted trees. We sould use an extra array for sizes of trees
Improvement 2: Path compression. Just after computing the root of p ,
                                 set the id of each examined node to point to that root

Time complexity:
Initialize: O(N)
Union: takes constant time, given roots
Find: takes time proportional to depth of p and q   O(N lgN)
"""

class UnionFind():
    """" Weighted  QuickUnion with Path Compression.  Coursera Sedgewick 1 w1"""
    def __init__(self, n):
        """ self.id is an array of integers
            self.id[i] is parent of i
            root of i is id[id[...id[i]...]]   # keep going until it doesn't change
        """
        self.id = [i for i in range(n)]         # the constructor: set id of each object to itself
        self.sz = [1,] * n                      # maintain extra array to count number of objects
                                                # in the tree rooted at i

    def root(self, i):
        """ root of i is id[id[...id[i]...]]   # keep going until it doesn't change """
        while i != self.id[i]:
            # Make every other node in path point to its grandparent
            # (there by halving path length)
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p, q):
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
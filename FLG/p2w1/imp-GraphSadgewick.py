class Graph():
    def __init__(self, v):
        """create an empty graph with V vertices"""
        pass


    def createFromInput(self, file):
        """create a graph from input stream"""
        pass

    def addEdge(self, v, w):
        """add an edge v-w"""
        pass

    def adj(self, v):
        """vertices adjacent to v"""
        pass

    def v_number(self):
        """number of vertices"""
        pass

    def e_number(self):
        """number of edges"""

    def toString(self):
        """string representation"""
        pass

    def degree(self, v):
        """compute the degree of v
        g: class Graph
        v: int
        """
        degree = 0
        for w in self.adj(v):
            degree += 1
        return degree

    def maxDegree(self, g, v):
        """compute maximum degree
        g: class Graph
        v: int
        """
        max = 0
        for v in range(self.v_number()):
            if self.degree(g, v) > max:
                max = self.degree(g, v)
        return max

    def averageDegree(self, g):
        """compute maximum degree
        g: class Graph
        """
        return 2.0 * self.e_number() / self.v_number()

    def numberOfSelfLoops(self, g):
        """count self-loops
        g: class Graph
        """
        count = 0
        for v in range(self.v_number()):
            for w in self.adj(v):
                if v == w:
                    count += 1
        return count/2             # each edge counted twice


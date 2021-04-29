class Graph():
    def __init__(self):
        """create an empty graph with V vertices"""
        self.graph = dict()     # empty graph
        self.v_num = 0          # Number of vertices
        self.e_num = 0          # Number of edges

        # for DFS
        self.marked = []      # marked[v] = true if v connected to s
        self.edgeTo = []      # edgeTo[v] = previous vertex on path from s to v


    def createFromFile(self, filename):
        """create a graph from input stream
        graph.txt:
        8     # Number of vertices
        7     # Number of edges
        0-1
        1 2
        2 3
        3 4
        4 5
        4 6
        4 7

        Data Structure for Graph: Dict of Sets
        0-1-2-3-4-5
              /\
             6  7
        graph = {1:{2},
                 2:{1,3},
                 3:{2,4},
                 4:{3,5,6,7},
                 5:{4},
                 6:{4},
                 7:{4}}
        """
        with open(filename) as f:
            lines = [line.rstrip() for line in f]
        self.v_num = m = int(lines[0])        # number of vertexes
        self.e_num = n = int(lines[1])        # number of edges

        self.marked = [False] * self.v_num # marked[v] = true if v connected to s
        self.edgeTo = [False] * self.v_num # edgeTo[v] = previous vertex on path from s to v

        for i in range(2, n+2):               # Start from 3rd line
            v1, v2 = map(int, lines[i].split())
            for v, u in (v1, v2), (v2, v1):
                if v not in self.graph:  # the set of neighbour vertexes is empty, create the set
                    self.graph[v] = {u}
                else:                   # the set of neighbour vertexes is nod empty, add new one
                    self.graph[v].add(u)

    def createFromdict(self, d, v, e):
        """create a graph from dict
            d = {'A': {'B'},
                'B': {'A','C'},
                'C': {'B','D'},
                'D': {'C'}
                }
        """
        self.graph = d
        self.v_num = v       # Number of vertices
        self.e_num = e       # Number of edges

    def addEdge(self, v, w):
        """add an edge v-w"""
        pass

    def adj(self, v):
        """Iterable<Integer: vertices adjacent to v"""
        for k in self.graph[v]:
            yield k

    # def v_number(self):
    #     """number of vertices"""
    #     pass

    # def e_number(self):
    #     """number of edges"""

    def toString(self):
        """string representation"""
        pass

    def degree(self, v):
       """compute the degree of v
       v: int
       :return int
       """
       return len(self.graph[v])

    def maxdegree(self):
        """compute maximum degree
        v: int
        """
        max = 0
        for v in self.graph.keys():
            if self.degree(v) > max:
                max = self.degree(v)
        return max

    def averagedegree(self):
        """compute avarage degree
        """
        return 2.0 * self.e_num / self.v_num

    def numberOfSelfLoops(self):
        """count self-loops"""
        count = 0
        for v in self.graph.keys():
            for w in self.graph[v]:
                if v == w:
                    count += 1
        return count/2             # each edge counted twice

    def dfs(self, v):
        """
        Recursive DFS does the work
        :param v:    vertex
        :return:
        """
        self.marked[v] = True
        for w in self.graph[v]:
            if not self.marked[w]:
                self.dfs(w)
                self.edgeTo[w] = v


def test_createFromFile():
    g = Graph()
    g.createFromFile('testgraph.txt')

def test_adj(g):
    for k in g.adj(4):
        print('4:', k)

def test_degree(g):
    return g.degree(4)

def test_maxdegree(g):
    return g.maxdegree()

def test_averagedegree(g):
    return g.averagedegree()

def test_numberOfSelfLoops(g):
    return g.numberOfSelfLoops()

def test_dfs(g):
    g.dfs(4)
    return g.marked

if __name__ == '__main__':
    g = Graph()
    g.createFromFile('testgraph.txt')

    # test_createFromFile()
    # test_adj(g)

    test_res = test_degree(g)
    # print('test_res', test_res)
    print("Test", 4, ":", "OK\n" if test_res == 4 else "Failed\n")

    test_res = test_maxdegree(g)
    # print('test_res', test_res)
    print("Test", 5, ":", "OK\n" if test_res == 4 else "Failed\n")

    test_res = test_averagedegree(g)
    # print('test_res', test_res)
    print("Test", 6, ":", "OK\n" if test_res == 1.75 else "Failed\n")

    test_res = test_numberOfSelfLoops(g)
    # print('test_res', test_res)
    print("Test", 7, ":", "OK\n" if test_res == 0.0 else "Failed\n")

    test_dfs(g)
    test_res = g.edgeTo
    # print('test_res', test_res)
    print("Test", 8, ":", "OK\n" if test_res == [1, 2, 3, 4, False, 4, 4, 4] else "Failed\n")








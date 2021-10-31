"""
Breadth-first search

In trying to traverse this graph breadth first, we will employ the use of a queue. The
algorithm creates a list to store the nodes that have been visited as the traversal process
proceeds. We shall start our traversal from node A.

Node A is queued and added to the list of visited nodes. Afterward, we use a while loop to
effect traversal of the graph. In the while loop, node A is dequeued. Its unvisited adjacent
nodes B, G, and D are sorted in alphabetical order and queued up. The queue will now
contain the nodes B, D, and G. These nodes are also added to the list of visited nodes. At
this point, we start another iteration of the while loop because the queue is not empty,
which also means we are not really done with the traversal.

Node B is dequeued. Out of its adjacent nodes A, F, and E, node A has already been visited.
Therefore, we only enqueue the nodes E and F in alphabetical order. Nodes E and F are then
added to the list of visited nodes.

Our queue now holds the following nodes at this point: D, G, E, and F. The list of visited
nodes contains A, B, D, G, E, F.

Node D is dequeued but all of its adjacent nodes have been visited so we simply dequeue it.
The next node at the front of the queue is G. We dequeue node G but we also find out that
all its adjacent nodes have been visited because they are in the list of visited nodes. Node G
is also dequeued. We dequeue node E too because all of its nodes have been visited. The
only node in the queue now is node F.

Node F is dequeued and we realize that out of its adjacent nodes B, D, and C, only node C
has not been visited. We then enqueue node C and add it to the list of visited nodes. Node C
is dequeued. Node C has the adjacent nodes F and H but F has already been visited, leaving
node H. Node H is enqueued and added to the list of visited nodes.

Finally, the last iteration of the while loop will lead to node H being dequeued. Its only
adjacent node C has already been visited. Once the queue is completely empty, the loop
breaks.

The output of the traversing the graph in the diagram is A, B, D, G, E, F, C, H.

In the worst-case scenario, each vertex or node and edge will be traversed, thus the time
complexity of the algorithm is O(|V| + |E|) , where |V| is the number of vertices or
nodes while |E| is the number of edges in the graph.
"""


from collections import deque

def bfs(graph, root):
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root

    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adj_nodes = graph[node]
        remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        if len(remaining_elements) > 0:
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)

    return visited_vertices

if __name__ == '__main__':
    # The adjacency list for the graph is as follows:
    graph = dict()
    graph['A'] = ['B', 'G', 'D']
    graph['B'] = ['A', 'F', 'E']
    graph['C'] = ['F', 'H']
    graph['D'] = ['F', 'A']
    graph['E'] = ['B', 'G']
    graph['F'] = ['B', 'D', 'C']
    graph['G'] = ['A', 'E']
    graph['H'] = ['C']

    print(bfs(graph, 'A'))


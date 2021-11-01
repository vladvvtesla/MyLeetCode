"""
Depth-first search

As the name suggests, this algorithm traverses the depth of any particular path in the graph
before traversing its breadth. As such, child nodes are visited first before sibling nodes. It
works on finite graphs and requires the use of a stack to maintain the state of the algorithm:

For continuity's sake, we are using a regular Python list as a stack.

The starting node, called root , is passed with the graph's adjacency matrix, graph. root is
pushed onto the stack. node = root holds the first node in the stack:

The body of the while loop will be executed provided the stack is not empty. If node is not
in the list of visited nodes, we add it. All adjacent nodes to node are collected by
adj_nodes = graph[node] . If all the adjacent nodes have been visited, we pop that node
from the stack and set node to graph_stack[-1] . graph_stack[-1] is the top node on
the stack. The continue statement jumps back to the beginning of the while loop's test
condition.

If, on the other hand, not all the adjacent nodes have been visited, the nodes that are yet to
be visited are obtained by finding the difference between the adj_nodes and
visited_vertices with the statement remaining_elements =
set(adj_nodes).difference(set(visited_vertices)) .

The first item within sorted(remaining_elements) is assigned to first_adj_node ,
and pushed onto the stack. We then point the top of the stack to this node.

When the while loop exists, we will return the visited_vertices .

Depth-first searches find application in solving maze problems, finding connected
components, and finding the bridges of a graph, among others.
"""


def dfs(graph, root):
    visited_vertices = list()
    graph_stack = list()
    graph_stack.append(root)
    node = root

    while len(graph_stack) > 0:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adj_nodes = graph[node]
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if len(graph_stack) > 0:
                node = graph_stack[-1]
            continue
        else:
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))

        first_adj_node = sorted(remaining_elements)[0]
        graph_stack.append(first_adj_node)
        node = first_adj_node

    return visited_vertices


if __name__ == '__main__':
    # The adjacency list for the graph is as follows:
    graph = dict()
    graph['A'] = ['B', 'S']
    graph['B'] = ['A']
    graph['S'] = ['A', 'G', 'C']
    graph['D'] = ['C']
    graph['G'] = ['S', 'F', 'H']
    graph['H'] = ['G', 'E']
    graph['E'] = ['C', 'H']
    graph['F'] = ['C', 'G']
    graph['C'] = ['D', 'S', 'E', 'F']

    print(dfs(graph, 'A'))


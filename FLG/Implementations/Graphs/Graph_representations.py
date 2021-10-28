"""
Graphs can be represented in two main forms.
1) Adjacency dict,
2) Adjacency matrix
"""
# 1. Adjacency dict
graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['E','A', 'C']
graph['C'] = ['A', 'B', 'E','F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']

# 2. Adjacency matrix
# Another approach by which a graph can be represented is by using an adjacency matrix. A
# matrix is a two-dimensional array. The idea here is to represent the cells with a 1 or 0
# depending on whether two vertices are connected by an edge.


matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)
adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
edges_list = []    # an edge between node A and B will be stored as (A, B).
for key in matrix_elements:
    for neighbor in graph[key]:
        edges_list.append((key,neighbor))
print('edges_list', edges_list)

# What needs to be done now is to fill the our multidimensional array by using 1 to mark the
# presence of an edge with the line
for edge in edges_list:
    index_of_first_vertex = matrix_elements.index(edge[0])
    index_of_second_vertex = matrix_elements.index(edge[1])
    adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1

print('adjacency_matrix', adjacency_matrix)
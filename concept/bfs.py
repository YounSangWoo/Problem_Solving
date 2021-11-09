def bfs(graph, start_node):
    visited, non_visited = list(), list()
    non_visited.append(start_node)

    while non_visited:
        node = non_visited.pop(0)
        if node not in visited:
            visited.append(node)
            non_visited.extend(graph[node])
    
    return visited

graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(bfs(graph, 'A'))

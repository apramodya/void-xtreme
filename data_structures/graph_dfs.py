from graph_ds import Graph
from stack_ds import Stack


def dfs(graph, start, end):
    s = Stack()

    start_vertex = graph.get_vertex(start)
    start_vertex.color == 'gray'
    s.push([start])

    while not s.is_empty():
        path = s.pop()
        last_vertex = graph.get_vertex(path[-1])
        if last_vertex.value == end:
            break
        for connection in last_vertex.connections:
            connected_vertex = graph.get_vertex(connection)
            if connected_vertex.color == 'white':
                connected_vertex.color = 'gray'
                new_path = path[::]
                new_path.append(connected_vertex.value)
                s.push(new_path)

        last_vertex.color = 'black'

    graph.reset_colors()
    return path


def df_traverse(graph, start):
    s = Stack()
    start_vertex = graph.get_vertex(start)
    s.push(start_vertex)
    start_vertex.color == 'gray'
    while not s.is_empty():
        vertex = s.pop()
        for node_val in vertex.connections:
            vert = graph.get_vertex(node_val)
            if vert.color == 'white':
                s.push(vert)
                vert.color = 'gray'
        print vertex.value
        vertex.color = 'black'

    graph.reset_colors()

g = Graph()

g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)

g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 5)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(3, 6)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(5, 6)

print g
print '-------------------------------------------------------'
df_traverse(g, 1)
print '-------------------------------------------------------'
print(dfs(g, 1, 6))

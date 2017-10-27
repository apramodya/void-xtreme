from graph_ds import Graph
from queue_ds import Queue


def bfs(graph, start, end):
    q = Queue()

    start_vertex = graph.get_vertex(start)
    start_vertex.color = 'gray'
    q.enqueue([start])

    while not q.is_empty():
        path = q. dequeue()
        last_vertex = graph.get_vertex(path[-1])
        if last_vertex.value == end:
            break
        else:
            for connection in last_vertex.connections:
                connected_vertex = graph.get_vertex(connection)
                if connected_vertex.color == 'white':
                    connected_vertex.color = 'gray'
                    new_path = path[::]
                    new_path.append(connected_vertex.value)
                    q.enqueue(new_path)

    graph.reset_colors()
    return path


def bf_traverse(graph, start):
    q = Queue()

    start_vertex = graph.get_vertex(start)
    print start_vertex.value
    start_vertex.color = 'gray'
    q.enqueue(start_vertex)

    while not q.is_empty():
        current_vertex = q.dequeue()
        for connection in current_vertex.connections:
            connected_vertex = graph.get_vertex(connection)
            if connected_vertex.color == 'white':
                print connected_vertex.value
                connected_vertex.color = 'gray'
                q.enqueue(connected_vertex)

    graph.reset_colors()













# Testing - Examples in the lecture slides for BFS
g = Graph()

g.add_vertex('r')
g.add_vertex('s')
g.add_vertex('t')
g.add_vertex('u')
g.add_vertex('v')
g.add_vertex('w')
g.add_vertex('x')
g.add_vertex('y')
g.add_vertex('z')

g.add_edge('r', 'v')
g.add_edge('r', 's')
g.add_edge('s', 'w')
g.add_edge('w', 't')
g.add_edge('w', 'x')
g.add_edge('t', 'u')
g.add_edge('t', 'x')
g.add_edge('x', 'y')
g.add_edge('u', 'y')

print g
print '-------------------------------------------------------'
bf_traverse(g, 's')
print '-------------------------------------------------------'
print bfs(g, 's', 'u')
print bfs(g, 's', 'y')

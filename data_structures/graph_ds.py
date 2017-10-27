class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = list()
        self.color = 'white'

    def __str__(self):
        return str(self.value) + "  " + str(self.connections) + " " + str(self.color)


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.root = None
        self.vertices = dict()
        self.size = 0

    def __str__(self):
        ret = ""
        for val, vertex in self.vertices.items():
            ret += '\n' + str(vertex.value) + "  " + str(vertex.connections) + " " + str(vertex.color)
        return ret

    def __len__(self):
        return self.size

    def __getitem__(self, item):
        return item in self.vertices

    def add_vertex(self, value):
        new_node = Vertex(value)
        self.vertices[value] = new_node
        self.size += 1

    def get_vertex(self, value):
        if value not in self.vertices:
            raise ValueError('There is no such vertex as ' + str(value))
        else:
            return self.vertices[value]

    def remove_vertex(self, value):
        if value not in self.vertices:
            raise ValueError('There is no such vertex as ' + str(value))

        del self.vertices[value]
        for key, vertex in self.vertices.items():
            vertex.connections.remove(value)

        self.size -= 1

    def add_edge(self, node1_value, node2_value):
        if node1_value not in self.vertices:
            raise ValueError('There is no such node as ' + str(node1_value))
        if node2_value not in self.vertices:
            raise ValueError('There is no such node as ' + str(node2_value))
        if node1_value in self.vertices[node2_value].connections:
            raise ValueError('A connection already exists between ' + str(node1_value) + ' and ' + str(node2_value))

        self.vertices[node1_value].connections.append(node2_value)

        if not self.directed:
            self.vertices[node2_value].connections.append(node1_value)

    def find_a_path(self, start_node, end_node, path=None):
        if path is None:
            path = []

        if start_node not in self.vertices:
            return None
        else:
            path.append(start_node)

            if start_node == end_node:
                return path

            for destination_node in self.vertices[start_node].connections:
                if destination_node not in path:
                    temp_path = self.find_path(destination_node, end_node, path)
                    if temp_path is not None:
                        return temp_path

            path.remove(start_node)
            return None

    def find_a_path_length(self, start_node, end_node):
        path = self.find_path(start_node, end_node)
        if path is not None:
            return len(path) - 1
        else:
            return None

    def reset_colors(self):
        for val, vertex in self.vertices.items():
            vertex.color = 'white'




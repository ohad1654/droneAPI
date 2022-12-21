import pickle
from Primitives.line import Line


class Graph:
    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict is None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
        """ returns a list of all the edges of a vertice"""
        return self._graph_dict[vertice]

    def all_vertices(self):
        """ returns the vertices of a graph as a set """
        return set(self._graph_dict.keys())

    def all_edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def remove_vertex(self,vertex):
        connected=self._graph_dict.pop(vertex)
        for v in connected:
            self._graph_dict[v].remove(vertex)



    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
        """
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                if y not in self._graph_dict[x]:
                    self._graph_dict[x].append(y)
            else:
                self._graph_dict[x] = [y]

    def dijkstra(self, src, dst):
        dist = {}
        prev = {}
        unvisitedVertex = self.all_vertices()
        for vertex in self.all_vertices():
            dist[vertex] = float('inf')
            prev[vertex] = None
        dist[src] = 0
        while unvisitedVertex:
            u = min(unvisitedVertex, key=lambda x: dist[x])  # the closest vertex to src
            unvisitedVertex.remove(u)
            for v in self.edges(u):
                alt = dist[u] + u.distance(v)
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

        if prev[dst] is None:
            raise Exception(str(dst) + "- Can't get there, pleas add points in uiMain!")

        path = []
        a = dst
        while a != src:
            path = [a] + path
            a = prev[a]
        return [src] + path

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return [Line(x.pop(), x.pop()) for x in edges]

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def remove_edge(self,edge):
        vertex1, vertex2 = tuple(edge)
        self._graph_dict[vertex1].remove(vertex2)
        self._graph_dict[vertex2].remove(vertex1)

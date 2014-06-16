""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""


class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError('Edges must connect exactly two vertices.')
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.

    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v, w):
        """Returns the edge between the two vertices if one exists,
        None otherwise.
        """
        try:
            return self[v][w]
        except:
            return None

    def remove_edge(self, e):
        """Removes all references of the given edge from the graph."""
        v, w = e
        del self[v][w]
        del self[w][v]

    def vertices(self):
        """Returns a list of all vertices in the graph."""
        return self.keys()

    def edges(self):
        """Returns a list of all edges in the graph."""
        edges = []
        for v in self.keys():
            for w in self[v].keys():
                if self[v][w] not in edges:
                    edges.append(self[v][w])

        return edges

    def out_vertices(self, v):
        """Returns a list of adjacent vertices to the given vertex."""
        adjacent_vertices = []
        for w in self[v].keys():
            if self[v][w]:
                adjacent_vertices.append(w)

        return adjacent_vertices

    def out_edges(self, v):
        """Returns a list of edges adjacent to the given vertex."""
        adjacent_edges = []
        for e in self.edges():
            if v in e:
                adjacent_edges.append(e)

        return adjacent_edges

    def add_all_edges(self):
        """Adds edges between all vertices of the graph."""
        for v in self.vertices():
            for w in self.vertices():
                self.add_edge(Edge(v, w))


def main(script, *args):
    v = Vertex('v')
    w = Vertex('w')
    x = Vertex('x')
    e = Edge(v, w)
    e2 = Edge(v, v)
    g = Graph([v, w, x], [e, e2])
    print g.out_vertices(v)
    g.remove_edge(e)
    g.add_all_edges()
    print g.out_edges(v)


if __name__ == '__main__':
    import sys
    main(*sys.argv)

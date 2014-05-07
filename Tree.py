__author__ = 'danbox'

from Graph import Graph
from LabeledUF import LabeledUF

class Tree(Graph):

    def __init__(self, num_verts, edge_list, root):
        if len(edge_list) is not num_verts - 1:
            Graph.__init__(self, 0, [])
        else:
            Graph.__init__(self, num_verts, edge_list)
            colored = [False] * num_verts
            self.dfs(root, colored)
            if False in colored:
                Graph.__init__(self, 0, [])
            else:
                self._root = root
                self._parent = [-1] * num_verts
                for index, vert in enumerate(self._verts):
                    for edge in vert:
                        self._parent[edge] = index

    def getRoot(self):
        return self._root

    def parent(self, i):
        return self._parent[i]

    def children(self, i):
        return self.neighbors(i)

    def __str__(self):
        if self.getn() is 0:
            return "Empty tree"
        else:
            return ''.join([str(super(Tree, self).__str__()), '\nroot: ', str(self.getRoot()), '\nparents: ', str(self._parent)])

    # Input is a set of ordered pairs giving the lca queries.
    # Return a list of lists, where the i^th list is a list of all j
    # such that the lca of {i,j} is desired
    def organizeQueries(self, queries):
        l = [[] for i in range(self.getn())]
        for i, j in queries:
            l[i].append(j)
            l[j].append(i)
        return l

    # main call to get things set up
    # The queries parameter is a list of pairs such as [(2,4), (1,3), (0,2)].
    # This means that the least common ancestors of {2,4}, ${1,3}$ and
    # {0,2} are asked for. # It returns a list of triples, (i,j,k), where
    # {i,j} is a query and k is the least common ancestor of i and j.
    def lca(self, queries):
        q = self.organizeQueries(queries)
        C = LabeledUF(self.getn())
        finished = [False]*self.getn()
        return self.lcaAux(self.getRoot(), finished, C, q, [])

    # recursive DFS augmented with union-find structure that resolves
    # the lca queries given in ’queries’. ’queries’ is organized
    # as follows: queries[i] is a list of all j such that the lca of {i,j}
    # is desired. C is a union-find data structure that each finished
    # node is in the same union-find class as its parent, and each
    # class containing black nodes is labeled with the highest node
    # in the class. Also, maintain the invariant that finished[j]
    # is True if the call on j has finished. Before the call on
    # i returns, for each j such that {i,j} is a query and j is finished,
    # it finds the least common ancestor k of {i,j} and appends
    # (i,j,k) to ’triples’. It returns the updated ’triples’
    # list.
    def lcaAux(self, i, finished, C, queries, triples):
        for j in queries[i]:
            if finished[j] is True:  # check if j is black
                C.union(i, j, C.findLabel(i))
                finished[i] = True
                triples.append((i, j, C.findLabel(i)))


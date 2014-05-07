__author__ = 'danbox'

class UF(object):
    ''' The elements to be unioned are numbered 0 through n-1.  Each
        identifier for a union-find class is also an interger from 0 through
        n-1.

        _id[i] tells id number of union-find class i is in
        _l[j] tells the list of elements for class j  '''

    # Get number of elements in the collection of union-find classes
    def getn(self):
        return len(self._l)

    # Initialize a union-find structure with elements {0, 1, ... n-1}, each
    #  initially in its own union-find class
    def __init__(self, n):
        self._id = range(n)
        self._l = [[i] for i in range(n)]

    # String representing current state of union-find structure.  Use is similar
    #  to that of toString() in Java.
    def __str__(self):
        return ''.join(['id:     ', str(self._id), '\nl:      ',  str(self._l), '\n'])

        # Find I.D. number of union-find class that currently contains element i
    def find(self, i):
        return self._id[i]

    # Return the members of the class containing i
    def classOf (self, i):
        return self._l[self.find(i)]

    # Check whether i and j are currently in the same union-find class.  If
    #  so, return false.  Otherwise, merge the union-find classes containing
    #  i and j.
    def union(self, i, j):
        id1, id2 = self.find(i), self.find(j)
        if id1 == id2:
            return False
        if len(self._l[id1]) < len(self._l[id2]):
            id1, id2 = id2, id1
        l1, l2 = self._l[id1], self._l[id2]
        for i in l2:
            self._id[i] = id1
        l1.extend(l2)
        self._l[id2] = None
        return True


if __name__ == '__main__':
    C = UF(10)
    print(C)

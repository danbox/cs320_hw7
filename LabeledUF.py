__author__ = 'danbox'

from UF import UF

# The following line makes the LabeledUF be a child of the UF class;
# it inherits its attributes, such as the 'union' and 'find' methods,
# and its instance variables ...


class LabeledUF(UF):
    '''
        The additional information that this class keeps is a label on
        each class giving satellite information about the class:
        self.findLabel(i) finds the label on the union-find class that
        contains i.  '''

    def __init__(self, n, initlabels = None):
        UF.__init__(self, n)      #call to parent class's constructor initializes
        # parent class's instances variables.  This doesn't
        # have to be the first statement of the constructor
        if initlabels == None:    #Default is to give each class an initial
            initlabels = range(n)  # label equal to the integer it contains
        self._label = initlabels[:]

    def __str__(self):
        return ''.join([str(super(LabeledUF, self).__str__()), '\nlabels: ', str(self._label)])

    def findLabel(self, i):
        return self._label[self.find(i)]

    def union(self, i, j, label = None):
        result = super(LabeledUF, self).union(i,j)
        self._label[self.find(i)] = label
        return result

if __name__ == '__main__':
    C = LabeledUF(10)
    print(C)
    C.union(3,5,'Frank')

    print(C)
    print ('The label of the class containing 5 is ' + str(C.findLabel(5)))

__author__ = 'danbox'

from time import time
import math
import random

'''
FORMATTING CONVENTION

The convention for formatting a list of points in this program is to use
a list of lists of pairs of floating-point values.  The first
element in each pair is the x coordinate of a point and the second
is its y coordinate.  There must be at least two points in a list.

Example:  [[3.2,5,8],[4.7,1.2]]
'''

'''
Read a set of points from a file.
Prconditions:  The file consists of two floating-point values per
  line, where the first gives the x coordinate of a point and the
  second gives its y coordinate.
Postconditions:  the returned list is a list of the points, adhering
  to the formatting convention (above)
'''
def readPts(filename):
    return []

'''
Merge of mergesort, for sorted lists of points.
Preconditions:  S1 and S2 are two lists of lists of size two, adhering
  to the formatting convention (above).  In addition, coord is either 0 or 1.
  If it is 0, then the two lists must be sorted by x coordinate
  and if it is 1, they must be sorted by y coordinate.
Postconditions:  The returned list is the union of the two lists.
  If coord == 0, it is sorted by x coordinate and if coord == 1, it
  is sorted by y coordinate.
'''
def mergePts(S1, S2, coord):
    return []

'''
Mergesort for a list of points.
preconditions:  S is a set of points adhering to the formatting convention
  (above), and coord is 0 or 1
postconditions:  if coord == 0, the returned list is the elements of S
  sorted by x coordinate, and if coord == 1, the returned list is the
  elements of S sorted by y coordinate.
'''
def msPts(S, coord):
    return []

'''
preconditions:  S is a set of points in two-space.
The two returned values are the square of the distance
between the closest pair of points, and a list of two points
adhering to the formatting convention (above), giving the closest
pair.

This is needed in the closest-pair algorithm for the base case where
 the number of points is two or three.  (Using this as the base case
 prevents us from having to consider what answer to return if there
 is only one point in the list).
'''
def brute(S):
    best = distsq(S[0], S[1])
    bestPair = [S[0], S[1]]
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            candidate = distsq(S[i], S[j])
            if candidate < best:
                best = candidate
                bestPair = [S[i], S[j]]
    return best, bestPair

'''
Find the closest pair in S

Precondition:  S conforms to the formatting convention, and no two points
  have the same x coordinate
Postcondition:  A tuple has been returned whose first element is the distance
squared, and whose second element is a list of two points.

This should generate two sorted lists and call closestAux
'''
def closest(S):
    return 0.0, [[0.0,0.0], [0.0,0.0]]

'''
preconditions:  X and Y are the same set of points in two-space, no
    two of which share the same x coordinate.
  X is sorted by X coordinate
  Y is sorted by Y coordinate
postconditions:  the returned tuple are the square of the distance of
  the closest pair and a list of size two giving the closest pair
'''
def closestAux(X, Y):
    return 0.0, [[0.0,0.0],[0.0,0.0]]

'''
Find the square of the distance between two points.
Preconditions:  p1 and p2 are lists of size two floating-point values,
  where the first element in each list is the x coordinate and the second
  is the y coordinate.
Postcondition:  the square of the distance between the two points has
  been returned
'''
def distsq(p1, p2):
    return 0.0

'''One way to test out the correctness and efficiency of your code is
to uncomment some of the following:
'''

''' ************************************* '''

''' S = readPts('points.txt')'''

'''
size = int(input("Enter number of points:  "))
print size
S = [[random.random(), random.random()] for i in range(size)]

start=time();
Soln = closest(S)
end = time();
print '\n    Solution for closest: ', Soln
print '\n     Elapsed for closest: ', end - start

start = time()
Soln = brute(S)
end = time()
print '\nSolution for brute-force: ', Soln
print '\n Elapsed for brute-force: ', end - start
'''
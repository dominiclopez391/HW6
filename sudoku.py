# ----------------------------------------------------------------------
# Name:     sudoku
# Purpose:  Homework6
#
# Author(s):
#
# ----------------------------------------------------------------------
"""
Sudoku puzzle solver implementation

q1:  Basic Backtracking Search
q2:  Backtracking Search with AC-3
q3:  Backtracking Search with MRV Ordering and AC-3
"""
import csp

# Enter your helper functions here


def build_csp(puzzle):
    """
    Create a Csp object representing the puzzle.
    :param puzzle: (dictionary) the dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: Csp object

    domains: a dictionary representing variables and their domains.
        The dictionary keys are variable names and the values are sets
        representing their domains.
    neighbors: a dictionary representing binary constraints.
        The dictionary keys are variable names and the values are sets
        containing all the variables that are connected to the key.
        (Variables are connected if they both appear in a constraint)
    constraint: a function that takes as arguments two variables
        and two values: f(var1, val1, var2, val2).
        The function returns True if var1 and var2 satisfy the
        constraint when their respective values are val1 and val2.
    """

    dictForCSP = {}
    for i in range(9):
        for j in range(9):
            if not (i, j) in puzzle:
                dictForCSP[(i, j)] = range(9)
            else:
                dictForCSP[(i, j)] = puzzle[(i, j)]

    neighborsForCSP = {}
    for i in range(9):
        for j in range(9):
            neighborsForCSP[(i, j)] = set()

            # add each element as a constraint

            #first 3x3 grid elements
            for k in range(3):
                for l in range(3):

                    #get every element in the corresponding 3x3 sudoku grid area for each variable
                    connectedVar = (((i - 1) // 3) * 3 + k, ((j - 1) // 3) * 3 + l);
                    if connectedVar != (i, j):
                        neighborsForCSP[(i, j)].add(connectedVar)

            #next row elements
            for k in range(9):
                if not (i, j) == (k, j) and not (k, j) in neighborsForCSP[(i, j)]:
                    neighborsForCSP[(i, j)].add((k, j))

            #next column elements
            for k in range(9):
                if not (i, j) == (i, k) and not (i, k) in neighborsForCSP[(i, j)]:
                    neighborsForCSP[(i, j)].add((i, k))
    pass


def q1(puzzle):
    """
    Solve the given puzzle with basic backtracking search
    :param puzzle: (dictionary) the dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    Csp object.
    """
    # Enter your code here and remove the pass statement below
    pass


def q2(puzzle):
    """
    Solve the given puzzle with backtracking search and AC-3 as
    a preprocessing step.
    :param puzzle: (dictionary) the dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    Csp object.
    """
    # Enter your code here and remove the pass statement below
    pass


def q3(puzzle):
    """
    Solve the given puzzle with backtracking search and MRV ordering and
    AC-3 as a preprocessing step.
    :param puzzle: (dictionary) the dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    Csp object.
    """
    # Enter your code here and remove the pass statement below
    pass

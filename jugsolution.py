#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# jugsolution.py
# Description:
# -----------------------------------------------------------------------------
#
# Started on <lun 20-02-2023 22:22:39.012449201 (1676928159)>
# Carlos Linares López <carlos.linares@uc3m.es>
#

"""
Definition of a solution to the water jugs problem
"""

# imports
# -----------------------------------------------------------------------------
import jugstate

# error messages
# -----------------------------------------------------------------------------
CRITICAL_WRONG_SOLUTION_LENGTH = "Solutions should consist of at least one state. Aborting ..."
CRITICAL_WRONG_ITEM_TYPE = "'{0}' is not an instance of a jug state"

# classes
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# JUGSolution
#
# Stores a solution to the water jugs problem as a list of states of JUGState
# -----------------------------------------------------------------------------
class JUGSolution(object):
    """Stores a solution to the water jugs problem as a list of states of
       JUGState

    """

    def __init__(self, states: list):
        """A solution is initialized with a list of states of JUGState"""

        # verify the list is not empty, that would not make any sense! Even if
        # one tries to solve a problem from the start state to it, the solution
        # should contain at least the start state
        if len(states) == 0:
            raise ValueError(CRITICAL_WRONG_SOLUTION_LENGTH)

        # also, verify the list consist of instances of jugstate
        for item in states:
            if not isinstance(item, jugstate.JUGState):
                raise TypeError(CRITICAL_WRONG_ITEM_TYPE)

        # initialize the data members of this container
        self._solution = states

        # also define data members for implementing iterators
        self._index = 0

    def __len__(self):
        """return the numbef of states in this solution, which is by definition
           equal to the step length plus one

        """

        return len(self._solution)

    def __iter__(self):
        """define the base case for iterators"""

        self._index = 0
        return self

    def __next__(self):
        """define the next step for iterators"""

        if self._index >= len(self._solution):
            raise StopIteration

        self._index += 1
        return self._solution[self._index - 1]

    def __str__(self):
        """return a string representation of this solution"""

        output = "{0}".format(self._solution[0])
        for istate in self._solution[1:]:
            output += " -- {0}".format(istate)

        # and return the output string
        return output

    def get_solution(self):
        """return the list of states of this solution"""

        return self._solution


# Local Variables:
# mode:python
# fill-column:80
# End:

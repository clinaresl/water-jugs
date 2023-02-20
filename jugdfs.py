#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# jugdfs.py
# Description:
# -----------------------------------------------------------------------------
#
# Started on <lun 20-02-2023 22:30:30.657082521 (1676928630)>
# Carlos Linares López <carlos.linares@uc3m.es>
#

"""Implementation of depth-first search (DFS) for solving the water jugs
problem

"""

# imports
# -----------------------------------------------------------------------------
import jugstate
import jugsolution

# error messages
# -----------------------------------------------------------------------------
CRITICAL_WRONG_START_TYPE = "The start state shall be an instance of a JUGState. Aborting ..."

# classes
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# JUGDFS
#
# Implementation of depth-first search (DFS) for solving the water jugs problem
# -----------------------------------------------------------------------------
class JUGDFS(object):
    """Implementation of depth-first search (DFS) for solving the water jugs
       problem

    """

    def __init__(self, start: jugstate.JUGState):
        """A solver of the water jugs problem using depth-first search is
           initialized with a start state which has to be an instance of a
           JUGState

        """

        # verify the type of the start state
        if not isinstance(start, jugstate.JUGState):
            raise TypeError(CRITICAL_WRONG_START_TYPE)

        # store the data members of this instance
        self._start = start

    def solve(self, state: jugstate.JUGState = None, path: list = []) -> jugsolution.JUGSolution:
        """apply depth-first search to solve this instance

           it returns the solution as an instance of JUGSolution

        """

        # depth-first search is implemented using a stack. For this, the system
        # stack used in recursive functions can be used, and thus, this solver
        # is implemented recursively. Note the two arguments to this function
        # are the current state (which might be None) and the path from the
        # start state.
        #
        # If the start state is not given, then the start given to the
        # constructor is used instead. When invoking this method for the first
        # time, the path shall be empty indeed. This provides a clear interface
        # to third-party users

        # importantly, depth-first search is generally invoked with a max_depth
        # parameter which bounds the maximum depth ---otherwise, the algorithm
        # might fall into an infinite loop. This is not necessary here, however,
        # since the underlying graph state is finite

        # first and foremost, if no state has been given then start with the
        # start state given to the constructor. Type verification skipped ...
        curr_state = state if state else self._start

        # base case - the current state is the goal state
        if curr_state.is_goal():

            # Yeah, solution found!!!! Build a solution from the path built
            # explicitly adding the start state. This is necessary because
            # originally the list is by default empty but it would be nice to
            # show the start state as well
            return jugsolution.JUGSolution([jugstate.JUGState(self._start.get_smaller(),
                                                              self._start.get_larger())] + path)

        # general case - expand this node and employ tail recursion to explore
        # the children
        children = curr_state.children()
        for child in children:

            # skip those cases where this child was already explored in the
            # current path
            if child in path:
                continue

            # recursively invoke this method over this child
            solution = self.solve(child, path + [child])

            # if a solution has been found, then abort the current iteration and
            # return it asap
            if isinstance(solution, jugsolution.JUGSolution):
                return solution

            # otherwise, keep on exploring children

        # at this point all children has been explored but no solution has been
        # generated. Return failure
        return None


# Local Variables:
# mode:python
# fill-column:80
# End:

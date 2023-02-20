#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# jugbfs.py
# Description:
# -----------------------------------------------------------------------------
#
# Started on <lun 20-02-2023 22:56:23.472577324 (1676930183)>
# Carlos Linares López <carlos.linares@uc3m.es>
#

"""Implementation of a solver of the water jugs problem using breadth-first
search

"""

# imports
# -----------------------------------------------------------------------------
import copy

import jugstate
import jugsolution

# error messages
# -----------------------------------------------------------------------------
CRITICAL_WRONG_START_TYPE = "The start state shall be an instance of JUGState. Aboring ..."

# classes
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# JUGBFS
#
# Implementation of a breadth-first search (BFS, not to confuse with best-first
# search) for solving the water jugs problem
# -----------------------------------------------------------------------------
class JUGBFS(object):
    """Implementation of a breadth-first search (BFS, not to confuse with
       best-first search) for solving the water problem jugs

    """

    def __init__(self, start: jugstate.JUGState):
        """A solver of the water jugs problem using breadth-first search is
           initialized with a start state which has to be an instance of a
           JUGState

        """

        # verify the type of the start state
        if not isinstance(start, jugstate.JUGState):
            raise TypeError(CRITICAL_WRONG_START_TYPE)

        # store the data members of this instance
        self._start = start

    def solve(self) -> jugsolution.JUGSolution:
        """apply breadth-first search to solve this instance

           it returns the solution as an instance of JUGSolution

        """

        # breadth-first search is implemented using a queue. In general, items
        # in the queue should be sorted in ascending order of their cost (and
        # some textbooks refer to this data structure as a priority queue). In
        # this case, however, all operators have the same cost (we say there is
        # no user-preference over their applicability and they are all equally
        # relevant/important), thus an ordinary list suffices for our purposes
        # as there is a bijection between depth and cost, so that inserting by
        # the back effectively sorts nodes in ascending order of their cost
        #
        # Note also, that because a queue is used, then this solver is *NOT*
        # implemented recursively but instead iteratively. Therefore, it does
        # not require any specific arguments as the start state is already given
        # to the constructor of this class
        #
        # Importantly, this implementation forces states to keep a copy of the
        # path from the start state to it. This is extraordinarily inefficient
        # and, instead, backpointers shall be used in the closed list
        # (implemented as a set below). this state space, however, is tiny (even
        # for large values of the maximum capacity of each jug) and thus this
        # approach has been preferred ---also for didactical purposes

        # -- initialization

        # first, initialize the path from the start with the start state itself
        self._start += self._start

        # populate the queue with the start state
        queue = [self._start]

        # create a closed list (implemented as a set) for storing all states
        # previously expanded ---duplicate detection!
        closed = set()

        # iterate until doomsday or the queue is exhausted
        while len(queue) > 0:

            # first, get the first node from the queue
            curr_state = queue.pop(0)

            # if this node is a goal, the return the solution immediately
            if curr_state.is_goal():

                # Yeah, we made it!!! Hoorrrayyy!!

                # the path to this solution consits of instances of JUGState.
                # There is something tricky here going around, if the path is
                # right away used to build the solution then each state,
                # independently printed would show the path leading to it, and
                # that's not what we want. Indeed, all we want is a list of
                # instances of JUGState which contain no path at all.
                # Comprehension lists come in handy ...
                solution =[jugstate.JUGState(state.get_smaller(), state.get_larger()) \
                           for state in curr_state.get_path()]
                return jugsolution.JUGSolution(solution)

            # otherwise, generate all children
            children = curr_state.children()

            # because the current state has been expanded add it to the closed
            # list
            closed.add(curr_state)

            # and add all children to the queue that has not been previously
            # expanded
            for child in children:

                if child not in closed:

                    # extend the path of this child with the current state
                    child.set_path(copy.deepcopy(curr_state.get_path()))
                    child += child
                    queue.append(child)

            # and go on until the queue is exhausted or a solution is found

        # at this point, the queue has been exhausted, so return failure
        return None


# Local Variables:
# mode:python
# fill-column:80
# End:

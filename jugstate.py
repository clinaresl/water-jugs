#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# jugstate.py
# Description:
# -----------------------------------------------------------------------------
#
# Started on <lun 20-02-2023 21:26:04.217052259 (1676924764)>
# Carlos Linares López <carlos.linares@uc3m.es>
#

"""
Definition of a state in the water jugs problem
"""

# imports
# -----------------------------------------------------------------------------

# error messages
# -----------------------------------------------------------------------------
CRITICAL_WRONG_VOLUME_TYPE = "The volume used either in the larger or smaller jug should be an int"
CRITICAL_WRONG_VOLUME_VALUE = "The volume used either in the larger or smaller jug exceeds its capacity"

# classes
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# JUGState
#
# Definition of a state in the water jugs problem
# -----------------------------------------------------------------------------
class JUGState(object):
    """Definition of a state in the water jugs problem"""

    # static attributes
    #
    # all instances of this class refer to different occupations of both water
    # jugs. Their capacity is therefore an invariant and can be stored as a
    # static attribute to be shared by all instances
    _smaller_capacity = 3
    _larger_capacity = 5

    def __init__(self, smaller: int, larger: int):
        """A state is initialized explicitly specifying the volume used in the
           smaller and larger jug, respectively

        """

        # well, both values should be ints, if not, halting ...
        if not isinstance(smaller, int) or not isinstance(larger, int):
            raise TypeError(CRITICAL_WRONG_VOLUME_TYPE)

        # likewise, if the volume used in either jug exceeds its capacity then
        # halting as well ...
        if smaller > JUGState._smaller_capacity or larger > JUGState._larger_capacity:
            raise ValueError(CRITICAL_WRONG_VOLUME_VALUE)

        # initialize the data members of this class
        self._smaller, self._larger = smaller, larger

        # some algorithms might require the state to store the path from the
        # start state to it. Initialize a data member to store this information
        # in case it is needed
        self._path = []


    def __add__(self, other):
        """add an instance of JUGState to this one, thus growing the path"""

        # append the new state to the path. Type verification skipped ...
        self._path.append(other)

        # and return this instance
        return self

    def __eq__(self, other) -> bool:
        """return True if and only if this instance is strictly equal to other"""

        # skipping type verification ...
        return self._smaller == other.get_smaller() and \
            self._larger == other.get_larger()

    def __hash__(self) -> int:
        """return the hash of this instance"""

        # states are likely to be used in frozensets or other structures
        # requiring a partial order. This is achieved by means of a hash code
        # which is then provided here
        return hash((self._smaller, self._larger))

    def __str__(self) -> str:
        """return a string representation of this instance"""

        output = "({0}, {1})".format(self._smaller, self._larger)

        # in case this instance contains a path, show it also
        if len(self._path) > 0:

            output += " [({0}, {1})".format(self._path[0]._smaller,
                                            self._path[0]._larger)
            for istate in range(1, len(self._path)):
                output += " -- ({0}, {1})".format(self._path[istate]._smaller, \
                                                  self._path[istate]._larger)
            output += "]"

        # and return the string representation
        return output

    def children(self) -> list:
        """return a list with all children of this instance, i.e., instances
           immediately accessible from this one by means of an operator

        """

        # -- initialization
        children = []

        # the "coding" (not programming!) of all operators is always the same:
        #
        #  if <precondds>
        #     then <postconditions>
        #
        # The preconditions verify that a specific operator is applicable to
        # this state. Note that some operators might have no preconditions,
        # though this is not the case in this domain
        #
        # The postconditions explicitly specify how to generate the child when a
        # specific operator is applicable

        # emptying jugs
        # ---------------------------------------------------------------------
        if self._smaller > 0:                                   # preconditions
            children.append(JUGState(0, self._larger))         # postconditions
        if self._larger > 0:                                    # preconditions
            children.append(JUGState(self._smaller, 0))        # postconditions

        # filling up
        # ---------------------------------------------------------------------
        if self._smaller < JUGState._smaller_capacity:          # preconditions
            children.append(JUGState(JUGState._smaller_capacity,
                                     self._larger))            # postconditions
        if self._larger < JUGState._larger_capacity:            # preconditions
            children.append(JUGState(self._smaller,            # postconditions
                                     JUGState._larger_capacity))

        # pouring from one jug to the other
        # ---------------------------------------------------------------------

        # The minimum between the volume in one jug and the available volume in
        # the other is the exact volume that can be poured

        # smaller -> larger
        volume = min(self._smaller, JUGState._larger_capacity - self._larger)
        if volume > 0:                                          # preconditions
            children.append(JUGState(self._smaller - volume,   # postconditions
                                     self._larger + volume))

        # larger -> smaller
        volume = min(self._larger, JUGState._smaller_capacity - self._smaller)
        if volume > 0:                                          # preconditions
            children.append(JUGState(self._smaller + volume,   # postconditions
                                     self._larger - volume))

        # return all children computed so far
        return children

    def get_smaller(self) -> int:
        """return the volume used in the smaller jug"""

        return self._smaller

    def get_larger(self) -> int:
        """return the volume used in the larger jug"""

        return self._larger

    def get_path(self) -> list:
        """return the path from the start state to this one"""

        return self._path

    def is_goal(self) -> bool:
        """return True if and only if this instance is a goal state"""

        return self._smaller == 4 or self._larger == 4


    def set_path(self, path: list):
        """set the path from the start state to this one as a list of instances
           of JUGState

        """

        self._path = path


# Local Variables:
# mode:python
# fill-column:80
# End:

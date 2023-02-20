#!/usr/bin/env python3
#
# jugs.py
# Description:
# -----------------------------------------------------------------------------
#
# Started on <lun 20-02-2023 21:12:07.477391691 (1676923927)>
# Carlos Linares López <carlos.linares@uc3m.es>
#

"""Solving the water jugs problem using search algorithms

"""

# imports
# -----------------------------------------------------------------------------
import jugbfs
import jugdfs
import jugparser
import jugstate

# error messages
# -----------------------------------------------------------------------------
CRITICAL_WRONG_MAX_VOLUME = "Maximum capacity has to be given as a strictly positive number"
CRITICAL_WRONG_INITIAL_VOLUMNE = "The initial volume of both jugs should be less or equal than its maximum capacity"

# main
# -----------------------------------------------------------------------------
def main():
    """main body"""

    # invoke the parser
    params = jugparser.JUGParser().parse()

    # in case the capacity of any jug has been modified, update it now
    if params.small is not None:
        if params.small <= 0:
            raise ValueError(CRITICAL_WRONG_MAX_VOLUME)
        jugstate.JUGState._smaller_capacity = params.small
    if params.large is not None:
        if params.large <= 0:
            raise ValueError(CRITICAL_WRONG_MAX_VOLUME)
        jugstate.JUGState._larger_capacity = params.large

    # create the initial state - in the initial state, both jugs are empty by
    # default but maybe the user came out with a different idea ;)
    if params.small_initial > jugstate.JUGState._smaller_capacity or \
       params.large_initial > jugstate.JUGState._larger_capacity:
        raise ValueError(CRITICAL_WRONG_INITIAL_VOLUME)
    start = jugstate.JUGState(params.small_initial, params.large_initial)

    # invoke the selected search algorithm
    solution = {
        "depth-first": jugdfs.JUGDFS(start).solve(),
        "breadth-first": jugbfs.JUGBFS(start).solve()
    }[params.algorithm]

    print(solution)


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    main()


# Local Variables:
# mode:python
# fill-column:80
# End:

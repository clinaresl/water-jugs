#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# jugparser.py
# Description:
# -----------------------------------------------------------------------------
#
# Started on <lun 20-02-2023 21:14:46.797876898 (1676924086)>
# Carlos Linares López <carlos.linares@uc3m.es>
#

"""
Parser of the CLI arguments
"""

# imports
# -----------------------------------------------------------------------------
import argparse
import sys

import version

# -----------------------------------------------------------------------------
# command parser of CLI arguments
# -----------------------------------------------------------------------------
class JUGParser(object):
    """command parser of CLI arguments"""

    def __init__(self):
        """Create the parser of the CLI arguments"""

        # initialize a parser for the water jugs problem
        self._parser = argparse.ArgumentParser(description=version.__description__)

        # mandatory arguments
        # ---------------------------------------------------------------------
        mandatory = self._parser.add_argument_group("Mandatory arguments", \
                                                    "The following arguments are required:")
        mandatory.add_argument('-x', '--algorithm',
                               choices=['depth-first', 'breadth-first'],
                               required=True,
                               help="search algorithm to use. Available options are 'depth-first' and 'breadth-first' search")

        # optional arguments
        # ---------------------------------------------------------------------
        optional = self._parser.add_argument_group("Optimal arguments", \
                                                    "The following arguments are optional:")
        optional.add_argument('-s', '--small',
                              type=int,
                              default=3,
                              help="capacity of the smaller jug. By default, 3 gallons")
        optional.add_argument('-l', '--large',
                              type=int,
                              default=5,
                              help="capacity of the larger jug. By default, 5 gallons")

        # Miscellaneous arguments
        # ---------------------------------------------------------------------
        misc = self._parser.add_argument_group('Miscellaneous')
        misc.add_argument('-V', '--version',
                          action='version',
                          version=" %s %s" % (sys.argv [0], version.__version__),
                          help="output version information and exit")

    def parse(self, args=None):
        """parse the arguments"""

        return self._parser.parse_args(args)


# Local Variables:
# mode:python
# fill-column:80
# End:

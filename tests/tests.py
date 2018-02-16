""" Test suite for practice_bidding. """

import sys
from os import path
import unittest


def _update_path():
    directory = path.dirname(path.realpath(__file__))
    # Need the directory two up from /practice_bidding.
    path_to_add = path.dirname(path.dirname(directory))
    print(f"Adding \"{path_to_add}\" to sys.path.")
    sys.path.append(path_to_add)


try:
    from practice_bidding.tests import parser_tests
    from practice_bidding.tests import xml_parser_tests
except ImportError:
    # This is in place for Travis. It is expected that under normal
    # circumstances the practice_bidding package will be found on sys.path.
    _update_path()

    from practice_bidding.tests import parser_tests
    from practice_bidding.tests import xml_parser_tests


def main():
    """ Run all unit tests in practice_bidding. """
    try:
        verbosity = int(sys.argv[1])
    except (ValueError, IndexError):
        verbosity = 1

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(parser_tests))
    suite.addTests(loader.loadTestsFromModule(xml_parser_tests))

    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)

    sys.exit(not result.wasSuccessful())


if __name__ == "__main__":
    main()

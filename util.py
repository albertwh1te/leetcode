"""
some utility for algorithms practice
"""
import unittest


class BaseTest(unittest.TestCase):
    pass


def equal(expect, reality):
    test = BaseTest()
    test.assertEqual(expect, reality)

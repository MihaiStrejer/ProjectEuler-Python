__author__ = 'Mihai'

from fractions import gcd


class DivHelpers:
    @staticmethod
    def lcm(a, b):
        """Calculate the lowest common multiple of two integers a and b"""
        return a * b // gcd(a, b)


_instDivHelpers = DivHelpers()
lcm = _instDivHelpers.lcm
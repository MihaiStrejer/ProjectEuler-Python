__author__ = 'Mihai'

from fractions import gcd


class MathHelpers:
    @staticmethod
    def lcm(a, b):
        """Calculate the lowest common multiple of two integers a and b"""
        return a * b // gcd(a, b)


_instDivHelpers = MathHelpers()
lcm = _instDivHelpers.lcm
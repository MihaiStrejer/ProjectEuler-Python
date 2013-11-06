__author__ = 'Mihai'

from Helpers.MathHelpers import DivHelpers
from functools import reduce

print(reduce(DivHelpers.lcm, range(1,21)))
__author__ = 'Mihai'

from Helpers.MathHelpers import lcm
from functools import reduce

print(reduce(lcm, range(1,21)))
from functools import reduce
from operator import mul

__author__ = 'Mihai'

from Helpers.PythagoreanHelpers import find_triplet_from_sum

result = find_triplet_from_sum(1000)

print(result)
print(reduce(mul, result, 1))
__author__ = 'Mihai'

from fractions import gcd


class PythagoreanHelper:
    @staticmethod
    def find_triplet_from_sum(triplet_sum):
        u = 2

        half_sum = triplet_sum / 2
        half_sum_sq_root = half_sum ** .5

        while u <= half_sum_sq_root:
            if half_sum % u == 0:
                if u % 2 == 0:
                    k = u + 1
                else:
                    k = u + 2

                o = triplet_sum / (2 * u)
                while k < 2 * u and k <= o:
                    if o % k == 0 and gcd(k, u) == 1:
                        d = triplet_sum / 2 / (k * u)
                        v = k - u
                        a = d * (u**2 - v**2)
                        b = 2 * d * u * v
                        c = d * (u**2 + v**2)
                        return a, b, c
                    k += 2
            u += 1


_inst = PythagoreanHelper()
find_triplet_from_sum = _inst.find_triplet_from_sum
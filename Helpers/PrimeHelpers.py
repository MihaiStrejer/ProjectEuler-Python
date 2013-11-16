__author__ = 'Mihai'


class PrimeHelper:
    @staticmethod
    def gen_primes():
        """ Generate an infinite sequence of prime numbers.    """
        # Source http://stackoverflow.com/a/568618
        # Maps composites to primes witnessing their compositeness.
        # This is memory efficient, as the sieve is not "run forward"
        # indefinitely, but only as long as required by the current
        # number being tested.
        #
        d = {}

        # The running integer that's checked for primeness
        q = 2

        while True:
            if q not in d:
                # q is a new prime.
                # Yield it and mark its first multiple that isn't
                # already marked in previous iterations
                #
                yield q
                d[q * q] = [q]
            else:
                # q is composite. D[q] is the list of primes that
                # divide it. Since we've reached q, we no longer
                # need it in the map, but we'll mark the next
                # multiples of its witnesses to prepare for larger
                # numbers
                #
                for p in d[q]:
                    d.setdefault(p + q, []).append(p)
                del d[q]

            q += 1

_inst = PrimeHelper()
gen_primes = _inst.gen_primes
__author__ = 'Mihai'

from Helpers.PrimeHelpers import gen_primes

count = 0
for prime in gen_primes():
    if count == 10000:
        print(prime)
        break

    count += 1
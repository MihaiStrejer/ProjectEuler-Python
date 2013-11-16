__author__ = 'Mihai'


from Helpers.PrimeHelpers import gen_primes

prime_sum = 0
for prime in gen_primes():
    if prime > 2000000:
        print(prime_sum)
        break
    prime_sum += prime
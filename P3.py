__author__ = 'Mihai'

number = 600851475143
division = 2
primeFactors = []

while number > 1:
    if number % division == 0:
        primeFactors.append(division)
        while number % division == 0:
            number /= division
    division += 1

print("Largest prime ", max(primeFactors))
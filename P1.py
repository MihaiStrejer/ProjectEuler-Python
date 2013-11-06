__author__ = 'Mihai'

numberSum = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        numberSum += i

print("Final sum", numberSum)
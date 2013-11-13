__author__ = 'Mihai'

numbers = range(1, 101)

sqSumOfNumbers = sum(numbers) ** 2

sumOfSqNumbers = 0
for i in numbers:
    sumOfSqNumbers += i ** 2

print("{} - {} = {}".format(sqSumOfNumbers, sumOfSqNumbers, sqSumOfNumbers - sumOfSqNumbers))
print()
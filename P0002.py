__author__ = 'Mihai'

count = 0
n1 = 1
n2 = 1
while n2 < 4000000:
    newNumber = n1 + n2
    n1 = n2
    n2 = newNumber
    if newNumber % 2 == 0:
        count += newNumber

print("Number", count)
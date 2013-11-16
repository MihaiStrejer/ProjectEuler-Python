__author__ = 'Mihai'


def reverse(num):
    return int("".join(list(reversed(str(num)))))


solution = []
for i in range(999, 99, -1):
    for x in range(999, 99, -1):
        number = i * x
        rev = reverse(number)

        if number == rev:
            solution.append(number)

print(max(solution))

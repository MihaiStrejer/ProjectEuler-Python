__author__ = 'Mihai'

from random import randint
from Helpers.ListHelpers import find_highest_numbers_indexes

# 0 = GO
# 2 = CC1       [CC]
# 7 = CH1           [CH]
# 10 = Jail             [J]
# 17 = CC2      [CC]
# 22 = CH2          [CH]
# 30 = G2J              [J]
# 33 = CC3      [CC]
# 36 = CH3          [CH]

# 5 = Rail1
# 15 = Rail2
# 25 = Rail3

# 12 = Util1
# 28 = Util2

cell_hits = [0] * 40
double_counter = 0
current_cell = 0

chance_counter = 0
community_counter = 0


def doCH():
    global chance_counter
    global current_cell

    if chance_counter < 6:
        current_cell = [0, 10, 11, 24, 39, 5][chance_counter]

    if chance_counter in [6, 7]:
        if current_cell == 7:
            current_cell = 15
        if current_cell == 22:
            current_cell = 25
        if current_cell == 36:
            current_cell = 5

    if chance_counter == 8:
        if current_cell == 22:
            current_cell = 28
        else:
            current_cell = 12

    if chance_counter == 9:
        current_cell -= 3

    chance_counter = (chance_counter + 1) % 16


def doCC():
    global community_counter
    global current_cell

    if community_counter < 2:
        current_cell = [0, 10][community_counter]

    community_counter = (chance_counter + 1) % 16


for i in range(0, 100000):
    d1 = randint(1, 4)
    d2 = randint(1, 4)

    if d1 == d2:
        double_counter += 1
    else:
        double_counter = 0

    if double_counter > 2:  # 3 doubles ... G2J
        current_cell = 10
        double_counter = 0
    else:
        current_cell = (current_cell + d1 + d2) % 40

        if current_cell in [7, 22, 36]:
            doCH()

        if current_cell in [2, 17, 33]:
            doCC()

        if 30 == current_cell:
            current_cell = 10  # G2J

    cell_hits[current_cell] += 1

highest_visited_cells = find_highest_numbers_indexes(cell_hits, 3)
print(cell_hits)
print("most visited cell numbers:", highest_visited_cells)

print("result:", "".join(str(n) for n in reversed(highest_visited_cells)))
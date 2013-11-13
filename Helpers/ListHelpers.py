__author__ = 'Mihai'


class ListHelpers:
    @staticmethod
    def find_highest_numbers_indexes(lst, k):
        """ Find the index of the n highest numbers in a list """
        return sorted(range(len(lst)), key=lambda x: lst[x])[-k:]

_instListHelpers = ListHelpers()
find_highest_numbers_indexes = _instListHelpers.find_highest_numbers_indexes
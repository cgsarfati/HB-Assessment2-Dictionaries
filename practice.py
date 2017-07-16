"""Dictionaries Practice

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    # turn list into set to remove duplicates, then convert back to list
    return set(list(words))


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    # convert each list to set to remove duplicates
    # do set arithmetic to find common words between sets, convert to list
    common_words = list(set(items1) & set(items2))

    # return list
    return common_words


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pairs summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    # create empty dict
    pair_sum_dict = {}

    # convert list to set to remove duplicates
    numbers = list(set(numbers))

    # add each pair of numbers to dict w/ k=pair and v=sum of items in pair
    # need key to be tuple first since list immutable -- != a key
    for first_number_pair in numbers:
        for second_number_pair in range(first_number_pair + 1, len(numbers)):
            pair_sum_dict[(first_number_pair, second_number_pair)] = first_number_pair + second_number_pair

    # create empty list
    pair_with_sum_0 = []

    # create pair, sum for loop; if sum==0, append pair to empty list
    for pair, pair_sum in pair_sum_dict:
        if pair_sum == 0:
            pair = list(pair)
            pair_with_sum_0.append(pair)

    return pair_with_sum_0
    # return list


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most in the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    # create empty dict
    character_count = {}

    # convert string to list of characters using split() -- removes spaces
    # if letter already a dict key, +=1; else, create new k:v pair w/ v = 1
    for word in phrase.split():
        for letter in word:
            if letter in character_count:
                character_count[letter] += 1
            else:
                character_count[letter] = 1

    # create key, value for loop; use max method to get highest value; if
    # value == highest, append key to empty list

    most_common_letter = []

    for character, count in character_count.items():
        if count == max(character_count.values()):
            most_common_letter.append(character)

    # return list
    return most_common_letter

#####################################################################
# You can ignore everything below this.


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print

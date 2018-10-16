#!/usr/bin/env python3

# Requirement for Python Upload 02 about lists and lambda and for each and ...:
#
# a) Comments required: Add your Name
#    remove this comments or other unused lines of code
# b) Return the longest word of a list in four different ways:
#    b1) longestWord_with_loop
#        loop through the list and....
#    b2) longestWord_with_recursion
#        # call a function again and again until ...
#    b3) longestWord_with_reduce
#        import functools
#        check out the reduce function: help(functools.reduce)
#    b4) longestWord_with_max
#        what is this optional 'key' parameter good for?
# c) for each solution add a comment about
#    c1) (+) advantage
#    c2) (-) disadvantage

# Kevin Gruber


def longestWord_with_loop(w):
    result = None

    longest_size = 0

    for word in w:
        if len(word) > longest_size:
            longest_size = len(word)
            longest_word = word

    result = longest_word

    # c1: (+) advantage: after "max" this is my favourite method of getting the longest_word from a list

    return result


def longestWord_with_recursion(wrds):
    result = None

    if len(wrds) == 1:
        result = wrds[0]
        return result

    elif len(wrds[0]) < len(wrds[1]):
        wrds.pop(0)
        return longestWord_with_recursion(words)

    elif len(wrds[0]) >= len(wrds[1]):
        wrds.pop(1)
        return longestWord_with_recursion(words)

    # c1: (+) advantage: simpole to read
    # c2: (-) disadvantage: longest method of solving
    return result


def longestWord_with_reduce(w):
    result = None

    import functools
    result = functools.reduce(lambda w, longest_word: w if len(w) > len(longest_word) else longest_word, w)

    # c2: (-) disadvantage: very nested method of solving and you have to import a library
    return result


def longestWord_with_max(w):
    result = None

    result = max(w, key=len)

    return result

    # My personal impression of this way to solve the problem
    # c1: (+) advantage: shortest way to get the longest word


# Just for testing the implemented functions:

# we create demo data
quotes = """The Scandal of education is that every time 
you teach something, you deprive a student of the pleasure 
and benefit of discovery.
(Seymour Papert, born February 29, 1928 died July 31 2016)

If debugging is the process of removing bugs, then programming 
must be the process of putting them in.
(Edsger W. Dijkstra)
"""
import re

# \W to substitute non-word-chars
quotes = re.sub(r'\W', ' ', quotes)
words = quotes.split()

# we test the functions with demo data
print(longestWord_with_loop(words))  # should print: ....
print(longestWord_with_recursion(words))  # should print: ....
print(longestWord_with_reduce(words))  # should print: ....
print(longestWord_with_max(words))  # should print: ....



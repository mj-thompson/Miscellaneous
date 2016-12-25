# Miscellaneous
I made this repository to hold some random side projects I developed or worked on.

##Words
I visited my parents for Christmas in 2016 and they've been doing some of the word jumbles in the LA Times for fun. I thought it would be fun to make a solver for them. Words.py is essentially a quick implementation of a brute-force solver. It tries all permutations of the given scrambled word and checks if they're in a supplied dictionary (words.txt). It will print the first match in the dictionary, which in most cases is correct. If the break line in the inner-most for-loop is taken out, it'll print all the possible solutions for a given word.

from itertools import permutations
from sys import argv
import pickle
import os.path

jumbled = argv[1:]

dict = []
answers = []


if os.path.exists("wordpic.pickl"):
    with open("wordpic.pickl") as f:
        dict = pickle.load(f)
else:
    with open("words.txt", 'r') as f:
        for line in f:
            dict.append(line.strip().lower())
    with open("wordpic.pickl", 'w') as f:
        pickle.dump(dict, f)

for scr in jumbled:
    perms = list(permutations(scr))
    i = 0
    for perm in perms:
        p = ''.join(perm)
        i = i+1
        if i % 20 == 0:
            print ("Checking permutation " + str(i) + " of " + str(len(list(perms))))
        if p in dict:
            print p
            answers.append(p)
            break


print ("Answers: " + " ".join(answers))

__author__ = 'SethUrban'
# We need to figure out the the 'rare' characters in the mess below from the page source
# i've inicluded this into the challenge_3_data.txt file

#1 - Need to open the file and read all the chars into a string
#2 - Go the string and count each time a new character comes up
#3 - Figure out the order of the rare characters
from array import *

fileText = open("challenge_3_data.txt", 'r')
scrambledText = fileText.read()

charsInScrambledText = array('c')
countCharInScrambledText = array('I')

for letter in scrambledText:
    if letter not in charsInScrambledText:
        charsInScrambledText.append(letter)
        countCharInScrambledText.append(0)
    else:
        index = charsInScrambledText.index(letter)
        countCharInScrambledText[index] += 1


for letter in charsInScrambledText:
    print letter + " "



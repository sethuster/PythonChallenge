__author__ = 'SethUrban'
#one small letter surrounded by exactly 3 big body gaurds on each of it's sides
#whatever the fuck that means. - Going to assume that this means a line at a time not on all sides
#since there would be four 'bodygaurds' if it were on all sides
import string

fileText = open("challenge_4_data.txt", 'r')
scrambledText = fileText.read()
lines = scrambledText.splitlines()

hiddenMessage = []

for i in range(len(scrambledText)):
    if scrambledText[i].isupper():
        if(scrambledText[i-1].islower() and scrambledText[i+1].isupper() and scrambledText[i+2].isupper()
        and scrambledText[i+3].islower() and scrambledText[i+4].isupper() and scrambledText[i+5].isupper()
        and scrambledText[i+6].isupper() and scrambledText[i+7].islower()):
            hiddenMessage.append(scrambledText[i+3])

print "".join(hiddenMessage)


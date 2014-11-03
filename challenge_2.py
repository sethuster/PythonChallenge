__author__ = 'SethUrban'
from array import *
import string

#we're trying to decode a message that has been displayed on the screen.
def Convert(message):
    convertedMessage = ""
    for letter in message:
        if letter not in alphabet:
            convertedMessage += letter
        else:
            alpha = alphabet.index(letter)
            alpha += 2
            if alpha == 26:
                alpha = 0
            if alpha == 27:
                alpha = 1
            convertedMessage += alphabet[alpha]
    return convertedMessage


alphabet = array('c', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
secretMessage = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp."
secretMessagePt2 = "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
secretMessage = secretMessage.upper()
secretMessagePt2 = secretMessagePt2.upper()

message1 = Convert(secretMessage)
message2 = Convert(secretMessagePt2)

print message1
print message2

dict = string.maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")
secretMessage = secretMessage.lower()
secretMessagePt2 = secretMessagePt2.lower()

message3 = secretMessage.translate(dict)
message4 = secretMessagePt2.translate(dict)
url = "map".translate(dict)

print message3
print message4
print url + ".html"
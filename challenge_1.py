__author__ = 'SethUrban'
# This is the python challenge from www.pythonchallenge.com
# The object is to use clues on the challenge URLS to find the URL for the next challenge
# First challenge URL: http://www.pythonchallenge.com/pc/def/0.html
ChallengeURL = "http://www.pythonchallenge.com/pc/def/{}.html"
URL = 2 ** 38
calculatedURL = str.format(ChallengeURL, str(URL))
print calculatedURL

#SUCESS
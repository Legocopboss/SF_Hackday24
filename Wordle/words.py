import random
from settings import *

#Unfiltered List
rawWordsList = [
    "jake",
    "statefarm",
    "tesing"
]

#Filtered List
wordsList = []

#Feature Flags
REPEAT = False
STANDARD = False
MAXLEN = 8


for i in range(len(rawWordsList)):
    currentWord = rawWordsList[i]

    #Settings logic
    lenCheck = len(currentWord) < MAXLEN
    repCheck =  "".join(dict.fromkeys(currentWord)) != currentWord
    standardCheck = len(currentWord) == 5 and repCheck

    #Flags if we must discard the word due to settings
    validWord = True

    if(not REPEAT and repCheck):
        validWord = False
    if(STANDARD and not standardCheck):
        validWord = False
    if(not lenCheck):
        validWord = False

    if(validWord):
        wordsList.append(currentWord)


def get_word():
    print(wordsList)
    return random.choice(wordsList)


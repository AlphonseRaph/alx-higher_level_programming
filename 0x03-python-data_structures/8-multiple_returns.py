#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence = "None"
        length = 0, sentence
        returntuple = (length[0], length[1])
        return returntuple
    else:
        returntuple = (len(sentence), sentence[0])
        return returntuple

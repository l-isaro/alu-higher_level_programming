#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        f_letter = sentence[0]
        length = len(sentence)
    else:
        f_letter = None
        length = 0
    return length, f_letter

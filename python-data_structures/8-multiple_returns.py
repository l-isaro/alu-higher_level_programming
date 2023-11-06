#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        f_letter = sentence[0]
        length = len(sentence)
        return length, f_letter
    else:
        f_letter = None
        return f_letter

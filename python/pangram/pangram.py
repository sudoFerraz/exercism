# -*- coding: utf-8 -*-

import sys

def is_pangram(sentence):
    """Defining if a string is a pangram."""

    list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',\
        'q','r','s','t','u','v','x','z']
    count = 0
    sentence = sentence.lower()

    for i in range(0, len(list)):
        for j in sentence:
            if list[i] == j:
                count = count + 1
                list[i] = '>'

    if count == 24:
        return True

    elif count < 24 or count > 24:
        return False

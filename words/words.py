# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :
__author__ = 'igor'

from word_parse import get_dictionary

def get_char_dict(word):
    d = {}
    for c in word:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    return d

def sortByLength(inputStr):
        return len(inputStr)

def get_good_words(word, length):
    words = get_dictionary()#['ар','арк','арка','окорок',]


    min_word_length = length
    from_word = word
    from_word_dict = get_char_dict(from_word)

    good_words = []
    for word_mean in words:
        word = word_mean["word"]
        if len(word) <= min_word_length*2:
            continue
        word_dict = get_char_dict(word)
        good = True
        for k in word_dict:
            if not k in from_word_dict or word_dict[k] > from_word_dict[k]:
                good = False
                break
        if good and not word in good_words:
            good_words.append(word_mean)

    good_words.sort(key=lambda k: len(k['word']), reverse=True)
    return good_words



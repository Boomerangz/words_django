import os
from untitled.settings import BASE_DIR

__author__ = 'igor'


def get_dictionary():
    file_from = os.path.join(BASE_DIR,"words", 'OZHEGOV.TXT')
    array=[]
    with open(file_from) as f:
        for line in f:
            line = line.split("|")
            str = line[0]
            str = str.split(",")[0]
            meaning = line[-1]
            array.append({"word":str,"meaning":meaning})
    return array


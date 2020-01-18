# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

def pig_it(text):
    return " ".join([i[1:] + i[0] + "ay" if i.isalpha() else i[1:] + i[0] for i in text.split()])

pig_it('This is my string')
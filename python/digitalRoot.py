# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

from functools import reduce

def digital_root(n):
    while n > 10:
        arrN = [int(i) for i in str(n)]
        n = reduce(lambda x, y: x + y, arrN)
    return n
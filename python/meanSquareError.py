#https://www.codewars.com/kata/51edd51599a189fe7f000015/train/python

from functools import reduce

def solution(array_a, array_b):
    f = [abs(array_a[i] - array_b[i])**2 for i in range(len(array_a))]
    return reduce(lambda x, y: x + y, f)/len(array_a)
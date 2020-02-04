# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def make_readable(seconds):
    s = seconds % 60
    m = int((seconds - s) / 60) % 60
    h = int(((seconds - s) / 60) /60)
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)
# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(array):
    x = [i for i in array if i is not 0 and str(i) != "0.0"]
    x.extend([0 for i in [i for i in array if i is 0 or str(i) == "0.0"]])
    return x
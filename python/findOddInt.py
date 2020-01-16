# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
      x = {}
      for i in seq:
          if i not in x:
              x[i] = 1
          elif i in x:
              x[i]+=1
      for i in x:
          if x[i] % 2 == 1:
              return i
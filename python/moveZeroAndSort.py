# https://www.codewars.com/kata/588a556d4b9a4bd09a000d1b/train/python

def sorted(lst):
      for j in range(len(lst)):
          for i in range(len(lst)):
              try:
                  if lst[i] > lst[i+1]:
                      lst[i], lst[i+1] = lst[i+1], lst[i]
              except: 
                  pass
      print(lst)
      return lst
    
def move_zeroes(*args):
    x = [i for i in sorted(list(args)) if i is not 0 and str(i) != "0.0"]
    x.extend([0 for i in [i for i in args if i is 0 or str(i) == "0.0"]])
    return x
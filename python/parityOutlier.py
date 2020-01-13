# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):
    x = []
    for i in integers[0:3]:
        x.append(abs(i) % 2)
    if x.count(1) > 1:
        for i in integers:
            if abs(i) % 2 == 0:
                return i
    else:
         for i in integers:
            if abs(i) % 2 == 1:
                return i
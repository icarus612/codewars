# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):
    x = [abs(i) % 2 for i in integers[0:3]]
    n = 0 if x.count(1) > 1 else 1
    for i in integers:
        if abs(i) % 2 == n:
            return i

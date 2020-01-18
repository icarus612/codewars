# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

def valid_parentheses(string):
    x = 0
    for i in string:
        if x < 0: 
            return False          
        if i == "(":
            x+=1
        elif i == ")":
            x-=1
    return x == 0
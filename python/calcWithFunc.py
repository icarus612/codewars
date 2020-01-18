# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

def zero(x=None): return 0 if x is None else eval('0{x}')
def one(x=None): return 1 if x is None else eval('1x')
def two(x=None): return 2 if x is None else eval('2x')
def three(x=None): return 3 if x is None else eval('3x')
def four(x=None): return 4 if x is None else eval('4x')
def five(x=None): return 5 if x is None else eval('5x')
def six(x=None): return 6 if x is None else eval('6x')
def seven(x=None): return 7 if x is None else eval('7x')
def eight(x=None): return 8 if x is None else eval('8x')
def nine(x=None): return 9 if x is None else eval('9x')

def plus(x): return f"+{x}"
def minus(x): return f"-{x}"
def times(x): return f"*{x}"
def divided_by(x): return f"/{x}"

print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))
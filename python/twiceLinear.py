# https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python

def dbl_linear(n):
    u = 1
    q2, q3 = [], []
    for i in range(n):
        q2.append(2 * u + 1)
        q3.append(3 * u + 1)
        u = min(q2[0], q3[0])
        if h == q2[0]: u = q2.pop(0)
        if h == q3[0]: u = q3.pop(0)
    return u
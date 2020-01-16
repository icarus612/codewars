# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python 

def create_phone_number(n):
    f = "".join(str(i) for i in n[:3])
    s = "".join(str(i) for i in n[3:6])
    t = "".join(map(str, n[-4:]))
    return f"({f}) {s}-{t}"
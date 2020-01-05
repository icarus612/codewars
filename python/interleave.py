#https://www.codewars.com/kata/523d2e964680d1f749000135

def interleave(*args):
    max_len = 0
    arr = []
    for i in args:
        if len(i) > max_len:
            max_len = len(i)
        
    for j in range(max_len):
        for i in args:
            try:
                arr.append(i[j])
            except:
                arr.append(None)
    return arr
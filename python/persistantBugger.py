#https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n):
    a = 0
    while n >= 10:
        a += 1
        final = 1
        x =[]
        for i in str(n):
            x.append(int(i))
        print(x)
        for i in x:
            final *= i
        n = final
        print(final)
    return a
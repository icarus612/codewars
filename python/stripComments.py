# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

def solution(string,markers):
    l = [(i-1 if string[i-1] is not "\n" and i-1 > 0 else i, string[i:].find(u"\u000A") + i if string[i:].find(u"\u000A") != -1 else -1) for i in range(len(string)) if string[i] in markers]
    x = []
    for i in range(len(l)):
        try:
            if l[i][1] == l[i+1][1]:
                l[i+1] = l[i]
        except IndexError:
            pass
    for i in l[::-1]:
        if x.count(i) == 0:
            x.append(i)
    for i in x:
        string = string[:i[0]] + string[i[1]:] if i[1] != -1 else string[:i[0]]
    print(x)
    return string
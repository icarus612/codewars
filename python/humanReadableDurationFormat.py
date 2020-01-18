# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_duration(seconds):
    format = ""    
    def form(t, w):
        return f"{t} {w}s, " if t > 1 else f"{t} {w}, "
        
    if seconds == 0:
        return "now"
    if seconds/31536000 >= 1:
        t = int(seconds/31536000)
        format += form(t, "year")
        seconds -= t * 31536000
    if seconds/86400 >= 1:
        t = int(seconds/86400)
        format += form(t, "day")
        seconds -= t * 86400
    if seconds/3600 >= 1:
        t = int(seconds/3600)
        format += form(t, "hour")
        seconds -= t * 3600
    if seconds/60 >= 1:
        t = int(seconds/60)
        format += form(t, "minute")
        seconds -= t * 60
    if seconds >= 1:
        t = seconds
        format += form(t, "second")
        seconds -= t
    format = format[:-2]
    l = 0
    format = format.split()
    for i in range(len(format)):
        try:
            int(format[i])
            l = i
        except: 
            pass
    
    if l > 0:
        format[l-1] = format[l-1][:-1]
        format.insert(l, "and")
    return " ".join(format)
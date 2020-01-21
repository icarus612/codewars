# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python

def rgb(r, g, b):
    return (format(max(min(r, 255), 0), "02x") + format(max(min(g, 255), 0), "02x") + format(max(min(b, 255), 0), "02x")).upper()
    
# no format function for easy conversion 
def rgb(r, g, b):
    r1, g1, b1 = int(r/16), int(g/16), int(b/16)
    r2, g2, b2 = r%16, g%16, b%16
    hex = [r1, r2, g1, g2, b1, b2]
    l = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    for x in range(len(hex)):
        if hex[x] > 15:
            hex[x], hex[x+1] = 15, 15
        if hex[x] >= 10:
            hex[x] = l[hex[x]]
        elif hex[x] < 0:
            hex[x], hex[x+1] = 0, 0  
    return "".join([str(i) for i in hex])
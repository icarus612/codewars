# https://www.codewars.com/kata/53f40dff5f9d31b813000774/train/python

def recoverSecret(triplets):
    place = {}
    for x in triplets:
        for i in range(3):
            if x[i] in place:
                place[x[i]] = i if place[x[i]] < i else place[x[i]]
            else:
                place[x[i]] = i
            
    for _ in range(len(triplets)):
        for x in triplets:
            for i in range(1, 3):
                if place[x[i - 1]] >= place[x[i]]:
                    place[x[i]] = place[x[i - 1]] + 1   
                    
    arr = ["" for i in range(len(place.keys()))]
    for x in place:
        arr[place[x]] = x
    return "".join(arr)
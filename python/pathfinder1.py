# https://www.codewars.com/kata/path-finder-number-1-can-you-reach-the-exit/train/python

def path_finder(maze):
    m = [list(i) for i in maze.split("\n")]
    visited = []
    to_visit = [(0,0)]
    end_block = (len(m)-1, len(m[0])-1)
    for x in to_visit:
        if x == end_block:
            return True
        if x not in visited:
            if x[0]+1 < len(m):
                if m[x[0]+1][x[1]] != "W":
                    to_visit.append((x[0]+1,x[1]))
            if x[0]-1 > 0:
                if m[x[0]-1][x[1]] != "W":
                    to_visit.append((x[0]-1,x[1]))
            if x[1]+1 < len(m[x[0]]):
                if m[x[0]][x[1]+1] != "W":
                    to_visit.append((x[0],x[1]+1))
            if x[1]-1 > 0:
                if m[x[0]][x[1]-1] != "W":
                    to_visit.append((x[0],x[1]-1))
            visited.append(x)
    return False

a = "\n".join([
".W.",
".W.",
"..."
])

b = "\n".join([
".W.",
".W.",
"W.."
])

c = "\n".join([
"......",
"......",
"......",
"......",
"......",
"......"
])

d = "\n".join([
"......",
"......",
"......",
"......",
".....W",
"....W."
])

print(path_finder(a))
print(path_finder(b))
print(path_finder(c))
print(path_finder(d))

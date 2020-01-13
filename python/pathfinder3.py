class Node:
    def __init__(self, v, c):
        self.value = v
        self.climb = c

def path_finder(maze):
    m = [list(i) for i in maze.split("\n")]
    visited = set()
    to_visit = [Node((0,0), -int(m[0][0]))]
    end_block = (len(m)-1, len(m[0])-1)
    for p in to_visit:
        x = p.value
        climb = c.climb.copy()
        if x == end_block:
            return p.climb
        climb +=
        if x not in visited:
            if x[0]+1 < len(m):
              to_visit.append(Node((x[0]+1,x[1]), path))
            if x[0]-1 >= 0:
                to_visit.append(Node((x[0]-1,x[1]), path))
            if x[1]+1 < len(m[x[0]]):
                to_visit.append(Node((x[0],x[1]+1), path))
            if x[1]-1 >= 0:
                to_visit.append(Node((x[0],x[1]-1), path))
        visited.add(x)
    return False

a = "\n".join([
  "000",
  "000",
  "000"
])

b = "\n".join([
  "010",
  "010",
  "010"
])

c = "\n".join([
  "010",
  "101",
  "010"
])

d = "\n".join([
  "0707",
  "7070",
  "0707",
  "7070"
])

e = "\n".join([
  "700000",
  "077770",
  "077770",
  "077770",
  "077770",
  "000007"
])

f = "\n".join([
  "777000",
  "007000",
  "007000",
  "007000",
  "007000",
  "007777"
])

g = "\n".join([
  "000000",
  "000000",
  "000000",
  "000010",
  "000109",
  "001010"
])

print(path_finder(a))
print(path_finder(b))
print(path_finder(c))
print(path_finder(d))
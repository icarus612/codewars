class Node:
    def __init__(self, v, p):
        self.value = v
        self.path = p

def path_finder(maze):
    m = [list(i) for i in maze.split("\n")]
    visited = set()
    to_visit = [Node((0,0), set())]
    end_block = (len(m)-1, len(m[0])-1)
    for p in to_visit:
        path = p.path.copy()
        x = p.value
        if x == end_block:
            m[x[0]][x[1]] = "x"
            for i in m: 
                print(i)
            return len(path)
        path.add(x)
        if x not in visited:
            if x[0]+1 < len(m):
                if m[x[0]+1][x[1]] != "W":
                    to_visit.append(Node((x[0]+1,x[1]), path))
            if x[0]-1 >= 0:
                if m[x[0]-1][x[1]] != "W":
                    to_visit.append(Node((x[0]-1,x[1]), path))
            if x[1]+1 < len(m[x[0]]):
                if m[x[0]][x[1]+1] != "W":
                    to_visit.append(Node((x[0],x[1]+1), path))
            if x[1]-1 >= 0:
                if m[x[0]][x[1]-1] != "W":
                    to_visit.append(Node((x[0],x[1]-1), path))
        visited.add(x)
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
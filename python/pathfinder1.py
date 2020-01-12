# https://www.codewars.com/kata/path-finder-number-1-can-you-reach-the-exit/train/python

def path_finder(maze):
	m = maze.split("\n")
	open_spaces = []
	to_visit = [(0,0)]
	end_block = (len(m)-1, len(m[0])-1)
	for i, y in enumerate(m):
		for j, x in enumerate(y):
			if x != "W":
				open_spaces.append((i, j))
	for x in to_visit:
		if x == end_block:
			return True
		if x in open_spaces:
			for i in open_spaces:
				if x[0] == i[0] and x[1]+1 == i[1]:
					to_visit.append(i)
				if x[0] == i[0] and x[1]-1 == i[1]:
					to_visit.append(i)
				if x[0]+1 == i[0] and x[1] == i[1]:
					to_visit.append(i)
				if x[0]-1 == i[0] and x[1] == i[1]:
					to_visit.append(i)
			open_spaces.remove(x)
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

# https://www.codewars.com/kata/path-finder-number-1-can-you-reach-the-exit/train/python
def path_finder(maze):
	m = maze.split("\n")
	open_spaces = []
	visited = []
	to_visit = [(0,0)]
	end_block = (len(m)-1, len(m[0])-1)
	def look_around(spot):
		for i in open_spaces:
			if spot[0] == i[0] and spot[1]+1 == i[1]:
				to_visit.append(i)
			if spot[0] == i[0] and spot[1]-1 == i[1]:
				to_visit.append(i)
			if spot[0]+1 == i[0] and spot[1] == i[1]:
				to_visit.append(i)
			if spot[0]-1 == i[0] and spot[1] == i[1]:
				to_visit.append(i)
	for i, y in enumerate(m):
		for j, x in enumerate(y):
			if x != "W":
				open_spaces.append((i, j))
	for i in to_visit:
		if i == end_block:
			return True
		if i not in visited:
			visited.append(i)
			look_around(i)

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

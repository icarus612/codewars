# https://www.codewars.com/kata/find-the-safest-places-in-town/train/python

def advice(agents, n):
    grid_dist = {}
    for i in agents.copy():
        if i[0] >= n or i[1] >= n:
            agents.remove(i)
    if len(agents) == n*n:
        return []
    for a in agents:
        for y in range(n):
            for x in range(n):
                d = abs(a[1] - y) + abs(a[0] - x)
                if (x, y) in grid_dist:
                    if d < grid_dist[(x,y)]:
                        grid_dist[(x,y)] = d
                else:
                    grid_dist[(x,y)] = d
    if len(agents) == 0: return [(x, y) for x in range(n) for y in range(n)]
    return [i for i in grid_dist if grid_dist[i] == max(grid_dist.values())] if len(grid_dist) > 0 else []
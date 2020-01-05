# https://www.codewars.com/kata/find-the-safest-places-in-town/train/python
def advice(agents, n):
    grid_dist = {}
    furthest = 0
    for i in agents.copy():
        if i[0] > n or i[1] > n:
            agents.remove(i)
    for a in agents:
        dist_a = a[0] + a[1]
        for y in range(n):
            for x in range(n):
                dist_b = x + y
                d = abs(dist_a - dist_b)
                try:
                    if d < grid_dist[(x,y)]:
                        grid_dist[(x,y)] = d
                except:
                    grid_dist[(x,y)] = d
                    
    for i in grid_dist:
        if grid_dist[i] > furthest:
            furthest = grid_dist[i]
        print(i, grid_dist[i])
    return ([i for i in grid_dist if grid_dist[i] == furthest])
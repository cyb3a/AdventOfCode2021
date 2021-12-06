from collections import defaultdict
input = [line.strip() for line in open('input/05.txt')]

grid = defaultdict(lambda: defaultdict(lambda: 0))
for l in input:
    a, b = l.split(' -> ')
    x1, x2 = list(map(int, a.split(',')))
    y1, y2 = list(map(int, b.split(',')))
    if x1 == y1:
        t1 = max(x2, y2)
        t2 = min(x2, y2)
        for i in range(t2, t1+1):
            grid[x1][i] += 1 if grid[x1][i] else 1
    elif x2 == y2:
        t1 = max(x1, y1)
        t2 = min(x1, y1)
        for i in range(t2, t1+1):
            grid[i][x2] += 1 if grid[i][x2] else 1

vals = [val for val in grid.values()]
v = [list(i.values()) for i in vals]
print(len([i for val in v for i in val if i > 1]))

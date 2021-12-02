input = [line.strip().split(' ') for line in open('input/02.txt')]
h, d = 0, 0

for dir, val in input:
    if dir == 'forward':
        h += int(val)
    elif dir == 'down':
        d += int(val)
    else:
        d -= int(val)

print(h * d)

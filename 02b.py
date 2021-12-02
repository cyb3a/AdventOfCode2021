input = [line.strip().split(' ') for line in open('input/02.txt')]
h, d, a = 0, 0, 0

for dir, val in input:
    if dir == 'forward':
        h += int(val)
        d += (a * int(val))
    elif dir == 'down':
        a += int(val)
    else:
        a -= int(val)

print(h * d)

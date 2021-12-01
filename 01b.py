input = [int(line.strip()) for line in open('input/01.txt')]
counter = 0
a, b, c = (1, 2, 3)
last_sum = input[a-1] + input[b-1] + input[c-1]
while c < len(input):
    new_sum = input[a] + input[b] + input[c]
    counter += 1 if new_sum > last_sum else 0
    last_sum = new_sum
    a = b
    b = c
    c += 1
print(counter)

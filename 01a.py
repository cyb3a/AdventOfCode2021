input = [int(line.strip()) for line in open('input/01.txt')]
counter = 0
for num in range(len(input)-1):
    counter += 1 if input[num+1] > input[num] else 0
print(counter)

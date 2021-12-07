from collections import defaultdict
input = list(map(int, open('input/07.txt').readline().strip().split(',')))
fuel_cost = defaultdict(lambda: 0)
for i in set(input):
    for crab in input:
        fuel_cost[i] += abs(crab-i)
print(min(fuel_cost.values()))

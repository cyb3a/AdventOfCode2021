import numpy as np
input = list(map(int, open('input/07.txt').readline().strip().split(',')))
i = np.floor(np.mean(input))
print(np.sum((np.abs(input - i) ** 2 + np.abs(input - i)) / 2))

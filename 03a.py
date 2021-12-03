import pandas as pd

input = [list(line.strip()) for line in open('input/03.txt')]
columns = list('abcdefghijkl')
df = pd.DataFrame(input, columns=columns)
gamma = ''.join(list(df.describe().loc['top']))
epsilon = gamma.replace('0', 'A').replace('1', '0').replace('A', '1')
print(int(gamma, 2) * int(epsilon, 2))

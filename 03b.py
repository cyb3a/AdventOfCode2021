import pandas as pd
from collections import Counter

input = [list(line.strip()) for line in open('input/03.txt')]
columns = list('abcdefghijkl')
df = pd.DataFrame(input, columns=columns)
oxy = df.copy()
oxy2 = []
co = df.copy()
co2 = []
for col in columns:
    cnt = Counter(oxy[col])
    max_value = '0'
    if cnt.get('1') == cnt.get('0'):
        max_value = '1'
    else:
        max_value = max(cnt, key=cnt.get)
    oxy = oxy[oxy[col] == max_value]
    oxy2.append(max_value)

for col in columns:
    cnt = Counter(co[col])
    min_value = '0'
    if cnt.get('1') == cnt.get('0'):
        min_value = '0'
    else:
        min_value = min(cnt, key=cnt.get)
    co = co[co[col] == min_value]
    co2.append(min_value)

print(int(''.join(oxy2), 2) * (int(''.join(co2), 2)))

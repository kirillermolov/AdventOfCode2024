#PART 1

import numpy as np

column1 = []
column2 = []
with open('input_file.txt') as file:
    for line in file:
        splitted_line = line.split()
        column1.append(int(splitted_line[0]))
        column2.append(int(splitted_line[1]))

column1 = np.array(column1)
column2 = np.array(column2)

print(np.sum(np.abs(np.sort(column1)-np.sort(column2))))

#PART 2

from collections import Counter

a = Counter(list(column2))
summa = 0
for i in column1:
   summa += i*a[i]

print(summa) 

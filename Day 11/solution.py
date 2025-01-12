#PART 1
import re

def blink(string,times):
    for i in range(0,times):
        string_splited = string.split()
        string_edited = [None] * len(string_splited)
        for pos, i in enumerate(string_splited):
            if i == '0':
               string_edited[pos] = '1'
            elif len(i)%2 == 0:
                start_part = i[0:int(len(i)/2)]
                end_part = i[int(len(i)/2):]
                if any(re.finditer('[1-9]', end_part)):
                    start_index = next(re.finditer('[1-9]', end_part)).start(0)
                    end_part = end_part[start_index:]
                else:
                    end_part = '0'
                string_edited[pos] = start_part+' '+end_part
            else:
                string_edited[pos] = str(int(i)*2024)

        string = " ".join(string_edited)
    return string

with open('input.txt','r') as file:
    input_string = file.readline().strip()

summa = 0
for i in input_string.split():
    string = blink(i,25)
    summa += len(string.split())

print(summa)

#PART 2

from collections import Counter

counter = Counter(input_string.split())

for i in range(75):
    new_counter = Counter()
    for item, value in counter.items():
        if item == '0':
            new_counter['1'] += value
        elif len(item)%2==0:

            new_counter[item[0:int(len(item)/2)]] += value
            new_counter[str(int(item[int(len(item)/2):]))] += value
        else:
            new_counter[str(2024*int(item))] += value

    counter = new_counter

print(counter.total())

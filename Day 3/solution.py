#PART 1
import re

with open('input.txt', 'r') as file:
    input_text = file.read()

pattern = 'mul\(\d+,\d+\)'

summa = 0
for i in re.findall(pattern, input_text):
    numbers = i[4:].split(',')
    summa += int(numbers[0])*int(numbers[1][0:-1])

print(summa)

#PART 2

with open('input.txt', 'r') as file:
    input_text = file.read()

pattern = 'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'

re.findall(pattern, input_text)

summa = 0
enabled = True
for i in re.findall(pattern, input_text):
     if re.search('don\'t\(\)',i):
         enabled = False
     elif re.search('do\(\)',i):
         enabled = True
     else:
         if enabled:
             numbers = i[4:].split(',')
             summa += int(numbers[0].strip())*int(numbers[1][0:-1])

print(summa)

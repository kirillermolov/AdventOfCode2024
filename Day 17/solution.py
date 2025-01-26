#PART 1

import math

register = {}
output = []

def get_comb_operand(operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return register['A']
    elif operand == 5:
        return register['B']
    elif operand == 6:
        return register['C']
    else:
        pass

def adv(operand):
     register['A'] = int(register['A']/math.pow(2,operand))

def bxl(operand):
    register['B'] = register['B']^operand

def bst(operand):
    register['B'] = operand%8

def jnz(operand):
    global instruction_pointer
    global index
    if register['A'] != 0:
        instruction_pointer = False
        index = operand

def bxc():
    register['B'] = register['B']^register['C']

def out(operand):
    output.append(str(operand%8))

def bdv(operand):
    register['B'] = int(register['A']/math.pow(2,operand))

def cdv(operand):
    register['C'] = int(register['A']/math.pow(2,operand))

with open('input.txt', 'r') as file:
    for line in file:
        if 'A' in line:
            register['A'] = int(line.split(':')[1].strip())
        elif 'B' in line:
            register['B'] = int(line.split(':')[1].strip())
        elif 'C' in line:
           register['C'] = int(line.split(':')[1].strip())
        else:
            if len(line.strip()) > 0:
                command = line.split(':')[1].strip()
                command = command.split(',')
index = 0
cont = True

while cont:
    instruction_pointer = True
    opcode = command[index]
    literal_operand = int(command[index+1])
    combo_operand = get_comb_operand(int(command[index+1]))

    if opcode == '0':
       adv(combo_operand)
    elif opcode == '1':
       bxl(literal_operand)
    elif opcode == '2':
       bst(combo_operand)
    elif opcode == '3':
       jnz(literal_operand)
    elif opcode == '4':
       bxc()
    elif opcode == '5':
       out(combo_operand)
    elif opcode == '6':
       bdv(combo_operand)
    else:
       cdv(combo_operand)
    if instruction_pointer:
        index = index + 2
    if index >= len(command)-1:
        cont = False

print(",".join(output))

#PART 2

from collections import defaultdict

lower_bound = 1
upper_bound = 8
level = len(command)-1
level_list = defaultdict(list)
level_list[len(command)].append(0)

while level >= 0:
    for bound in level_list[level+1]:
        if level+1 == len(command):
            upper_bound = 8
            lower_bound = 1
        else:
            upper_bound = (bound+1)*8
            lower_bound = bound*8

        for i in range(lower_bound,upper_bound):
          if level ==  len(command)-1:
              check = ( ((i^1)^4)^(int(i/math.pow(2,i^1)))  )%8
          else:
              check = ( (((i%8)^1)^4)^(int(i/math.pow(2,(i%8)^1)))  )%8
          if check == int(command[level]):
              level_list[level].append(i)
    level -= 1

level_list[0].sort()
print(level_list[0][0])

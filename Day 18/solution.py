#PART 1

from collections import defaultdict

count = 0
list_coordinates = []
with open('input.txt') as file:
    for line in file:
        splitted = line.strip().split(',')
        list_coordinates.append(complex(int(splitted[1]), int(splitted[0])))
        count += 1
        if count == 1024:
            break

def default_value():
    return '#'

position_dictionary = defaultdict(default_value)

for row in range(71):
    for column in range(71):
        if complex(row,column) in list_coordinates:
           position_dictionary[complex(row,column)] = '#'
        else:
            position_dictionary[complex(row,column)] = '.'

direction_list = [1,-1,complex(0,1),complex(0,-1)]
position_score = defaultdict(lambda: defaultdict(int))


def calculate_score(income_direction, position):
    for direction in direction_list:
        if direction == -income_direction:
            continue
        if position_dictionary[position+direction] != '#':
            pos_score = position_score[position][income_direction] + 1
            if position_score[position+direction][direction] == 0 or pos_score < position_score[position+direction][direction]:
                position_score[position+direction][direction] = pos_score
                list_to_process.append((direction, position+direction))
                return True

list_to_process = []
list_to_process.append((2, complex(0,0)))
to_continue = True
while to_continue:
    to_continue = False
    for item in list_to_process:
        if calculate_score(item[0],item[1]):
            to_continue = True

print(min( position_score[complex(70,70)].values() ) )

#PART 2

list_coordinates = []
with open('input.txt') as file:
    for line in file:
        splitted = line.strip().split(',')
        list_coordinates.append(complex(int(splitted[1]), int(splitted[0])))

def create_dictionaries(end):
    position_dictionary = defaultdict(default_value)
    position_score = defaultdict(lambda: defaultdict(int))
    for row in range(71):
        for column in range(71):
            if complex(row,column) in list_coordinates[0:end+1]:
               position_dictionary[complex(row,column)] = '#'
            else:
                position_dictionary[complex(row,column)] = '.'
    return position_dictionary, position_score

def calculate_score(income_direction, position,list_to_process):
    for direction in direction_list:
        if direction == -income_direction:
            continue
        if position_dictionary[position+direction] != '#':
            pos_score = position_score[position][income_direction] + 1
            if position_score[position+direction][direction] == 0 or pos_score < position_score[position+direction][direction]:
                position_score[position+direction][direction] = pos_score
                list_to_process.append((direction, position+direction))
                return True


def search():
    list_to_process = []
    list_to_process.append((2, complex(0,0)))
    to_continue = True
    while to_continue:
        to_continue = False
        for item in list_to_process:
            if calculate_score(item[0],item[1],list_to_process):
                to_continue = True

    return len( position_score[complex(70,70)].values() ) == 0

begin = 1024
end = len(list_coordinates)
middle = begin + (end-begin)//2
found = False

while middle - begin != 1:
    position_dictionary, position_score = create_dictionaries(middle)
    found = search()
    if found:
        end = middle
        middle = begin + (end-begin)//2
    else:
        begin = middle
        middle = begin + (end-begin)//2

for i in [begin,middle,end]:
    position_dictionary, position_score = create_dictionaries(middle)
    found = search()
    if found:
        break

print(str(int(list_coordinates[i].imag)) + ',' + str(int(list_coordinates[i].real)))

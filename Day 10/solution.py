#PART 1

def parse_input(path):
    with open(path, "r") as input:
        return {
            complex(row_ix, col_ix): int(char)
            for row_ix, row in enumerate(input)
            for col_ix, char in enumerate(row.strip())
        }


position_dictionary = parse_input('input.txt')
direction_list = [1,-1,complex(0,1),complex(0,-1)]

def move(coordinate,direction):
    try:
        if position_dictionary[coordinate+direction]-position_dictionary[coordinate] != 1:
            return False
        else:
            if position_dictionary[coordinate+direction] == 9 and coordinate+direction not in reached_list:
                reached_list.append(coordinate+direction)
                return True
    except:
        return False
    coordinate = coordinate+direction
    for direction in direction_list:
        move(coordinate,direction)


start_index = 0
start_position_coordinates = []
position_keys = list(position_dictionary.keys())
position_values = list(position_dictionary.values())
while True:
    try:
       index_found = position_values.index(0,start_index)
       start_position_coordinates.append(position_keys[index_found])
       start_index = index_found + 1

    except:
        break

summa = 0
for start_position in start_position_coordinates:
    reached_list = []
    for direction in direction_list:
        move(start_position,direction)
    summa += len(reached_list)

print(summa)

#PART 2

def move(coordinate,direction):
    global summa
    try:
        if position_dictionary[coordinate+direction]-position_dictionary[coordinate] != 1:
            return False
        else:
            if position_dictionary[coordinate+direction] == 9:
                summa = summa+1
                return True
    except:
        return False
    coordinate = coordinate+direction
    for direction in direction_list:
        move(coordinate,direction)


start_index = 0
start_position_coordinates = []
position_keys = list(position_dictionary.keys())
position_values = list(position_dictionary.values())
while True:
    try:
       index_found = position_values.index(0,start_index)
       start_position_coordinates.append(position_keys[index_found])
       start_index = index_found + 1

    except:
        break

summa = 0
for start_position in start_position_coordinates:
    for direction in direction_list:
        move(start_position,direction)

print(summa)

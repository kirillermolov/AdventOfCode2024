#PART 1

def move(position,direction):
    if position_dict[position + direction] == '.':
        position_dict[position + direction] = position_dict[position]
        position_dict[position] = '.'
        return True
    elif position_dict[position + direction] == '#':
        return False
    else:
        if move(position+direction, direction):
            position_dict[position + direction] = position_dict[position]
            position_dict[position] = '.'
            return True
        else:
            return False


direction_dict = {'^':-1,'v':1,'<':complex(0,-1),'>':complex(0,1)}
position_dict = {}

with open('input.txt') as file:
    for row, string in enumerate(file):
        if ('^' in string) or ('v' in string) or  ('<' in string) or ('>' in string):
            for val in string.strip():
                for robot_position in position_dict.keys():
                    if position_dict[robot_position] == '@':
                        break
                move(robot_position,direction_dict[val])
                label = "Move "+val
                #print(label)
                #visualize()
        else:
            for column, val in enumerate(string.strip()):
                position_dict[complex(row,column)] = val

summa = 0
for position in position_dict.keys():
    if position_dict[position] == 'O':
         summa += 100*position.real + position.imag

print(summa)

#PART 2

def move_robot(position,direction):
    if position_dict[position + direction] == '.':
        position_dict[position + direction] = position_dict[position]
        position_dict[position] = '.'
        return True
    elif position_dict[position + direction] == '#':
        return False
    else:
        if move_box(position+direction, direction, False):
            position_dict[position + direction] = position_dict[position]
            position_dict[position] = '.'
            return True
        else:
            return False

def move_box_vertically(position, direction, neighbour,test=False):
    position_dict[position + direction] = position_dict[position]
    position_dict[position] = '.'
    position_dict[position + direction + neighbour] = position_dict[position+neighbour]
    position_dict[position+neighbour] = '.'


def move_box(position,direction,test=False):
    if direction == 1 or direction == -1:
        if position_dict[position] == '[':
           neighbour = complex(0,1)
        else:
            neighbour = complex(0,-1)
        if position_dict[position + direction] == '.' and position_dict[position + neighbour + direction] == '.':
            if not test:
                move_box_vertically(position, direction, neighbour, test)
            return True
        elif position_dict[position + direction] == '#' or position_dict[position +  neighbour + direction] == '#':
            return False
        else:
            if position_dict[position + direction] == '.' or position_dict[position + neighbour + direction] == '.':
                if position_dict[position + direction] != '.':
                    if move_box(position+direction, direction, test):
                        if not test:
                            move_box_vertically(position, direction, neighbour,test)
                        return True
                    else:
                        return False
                else:
                    if move_box(position+direction+neighbour, direction, test):
                        if not test:
                            move_box_vertically(position+neighbour, direction, -neighbour,test)
                        return True
                    else:
                        return False
            else:
                if position_dict[position + direction] != position_dict[position]:

                    check_value1 = move_box(position+direction+neighbour,direction,True)
                    check_value2 = move_box(position+direction, direction,True)

                    if check_value1 and check_value2 and test:
                        return True
                    elif check_value1 and check_value2 and not test:
                        move_box(position+direction, direction)
                        move_box(position+direction+neighbour,direction)
                        move_box_vertically(position, direction, neighbour)
                        return True
                    else:
                        return False

                else:
                    if move_box(position+direction, direction,test):
                        if not test:
                            move_box_vertically(position, direction, neighbour,test)
                        return True
                    else:
                        return False
    else:
        if position_dict[position + direction] == '.':
            position_dict[position+direction] = position_dict[position]
            position_dict[position] = '.'
            return True
        elif position_dict[position + direction] == '#':
            return False
        else:
            if move_box(position+direction,direction):
                position_dict[position+direction] = position_dict[position]
                position_dict[position] = '.'
                return True
            else:
                return False

with open('input.txt') as file:
    for row, string in enumerate(file):
        column = 0
        if ('^' in string) or ('v' in string) or  ('<' in string) or ('>' in string):
            for val in string.strip():
                for robot_position in position_dict.keys():
                    if position_dict[robot_position] == '@':
                        break
                move_robot(robot_position,direction_dict[val])
        else:
            for val in string.strip():
                if val == 'O':
                    position_dict[complex(row,column)] = '['
                    column += 1
                    position_dict[complex(row,column)] = ']'
                    column += 1
                elif val == '#' or val == '.':
                    position_dict[complex(row,column)] = val
                    column += 1
                    position_dict[complex(row,column)] = val
                    column += 1
                else:
                    position_dict[complex(row,column)] = val
                    column += 1
                    position_dict[complex(row,column)] = '.'
                    column += 1
            if column != 0:
                max_column = column

summa = 0
for position in position_dict.keys():
    if position_dict[position] == '[':
        if position.real < max_column/2:
            summa += 100*position.real + position.imag
        else:
            summa += 100*position.real + max_column-position.imag-1

print(summa)

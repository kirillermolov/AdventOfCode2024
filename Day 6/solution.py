#PART 1

import numpy as np

def create_matrix_from_file(file_name):
    matrix = []
    with open(file_name,'r') as file:
        for i in file:
           row = [char for char in i if char != '\n']
           matrix.append(row)

    return np.array(matrix)

def make_step(matrix, direction, coordinates_row, coordinates_column):
    matrix[coordinates_row,coordinates_column] = 'X'
    new_coordinates_row = coordinates_row
    new_coordinates_column = coordinates_column
    if direction == 'up':
        new_coordinates_row -= 1
        new_direction = 'right'
    elif direction == 'down':
        new_coordinates_row += 1
        new_direction = 'left'
    elif direction == 'right':
        new_coordinates_column += 1
        new_direction = 'down'
    else:
        new_coordinates_column -= 1
        new_direction = 'up'
    if not (new_coordinates_column < 0 or new_coordinates_column >= np.shape(matrix)[1] or new_coordinates_row >= np.shape(matrix)[0] or new_coordinates_row < 0):
        if matrix[new_coordinates_row, new_coordinates_column] == '#':
            return matrix, new_direction, coordinates_row, coordinates_column
        else:
            return matrix, direction, new_coordinates_row, new_coordinates_column
    else:
        return matrix, -1, -1, -1


matrix = create_matrix_from_file('input.txt')

possible_guadrd_direction = ['^', '>', 'v', '<']
directions = ['up', 'right', 'down', 'left']

for pos, i in enumerate(possible_guadrd_direction):
    if np.size(np.where(matrix == i)[0]) != 0:
        guard_row = np.where(matrix == i)[0][0]
        guard_column = np.where(matrix == i)[1][0]
        direction = directions[pos]
        break

while guard_row >= 0:
     matrix, direction, guard_row, guard_column = make_step(matrix, direction, guard_row, guard_column)

print(len(np.where(matrix.flatten()== 'X')[0]))

#PART 2

import copy

def check_cycle(direction, coordinates_row, coordinates_column):
    global path_string
    start_index = 0
    path_before_hitting = None
    while start_index >= 0:
        start_index = path_string.find(str(coordinates_row) + str(coordinates_column) + direction, start_index)
        if start_index > 0:
            path_before_hitting = path_string[start_index:]
            start_index += 1
    saved_path = path_dict.get(coordinates_row*column + coordinates_column, set())
    if path_before_hitting in saved_path:
        return True
    else:
        if path_before_hitting:
            if path_dict.get(coordinates_row*column + coordinates_column, set()):
               path_dict.get(coordinates_row*column + coordinates_column).add(path_before_hitting)
            else:
                path_dict[coordinates_row*column + coordinates_column] = {path_before_hitting}
        return False

def make_step(matrix, direction, coordinates_row, coordinates_column):
    global path_string
    matrix[coordinates_row,coordinates_column] = 'X'
    path_string += str(coordinates_row) + str(coordinates_column)
    new_coordinates_row = coordinates_row
    new_coordinates_column = coordinates_column
    if direction == 'up':
        new_coordinates_row -= 1
        new_direction = 'right'
    elif direction == 'down':
        new_coordinates_row += 1
        new_direction = 'left'
    elif direction == 'right':
        new_coordinates_column += 1
        new_direction = 'down'
    else:
        new_coordinates_column -= 1
        new_direction = 'up'
    if not (new_coordinates_column < 0 or new_coordinates_column >= np.shape(matrix)[1] or new_coordinates_row >= np.shape(matrix)[0] or new_coordinates_row < 0):
        if matrix[new_coordinates_row, new_coordinates_column] == '#':
           if check_cycle(direction,coordinates_row,coordinates_column):
               return None, None, -1, -1, -1, True
           else:
                path_string += direction
                return matrix, path_string, new_direction, coordinates_row, coordinates_column, False
        else:
            return matrix, path_string, direction, new_coordinates_row, new_coordinates_column, False
    else:
        return matrix, path_string, -1, -1, -1, False


matrix_clear = create_matrix_from_file('input.txt')
column = np.shape(matrix_clear)[1]

possible_guadrd_direction = ['^', '>', 'v', '<']
directions = ['up', 'right', 'down', 'left']

for pos, i in enumerate(possible_guadrd_direction):
    if np.size(np.where(matrix_clear == i)[0]) != 0:
        guard_start_row = np.where(matrix_clear == i)[0][0]
        guard_start_column = np.where(matrix_clear == i)[1][0]
        guard_start_direction = directions[pos]
        break


coordinates = np.where(matrix == 'X')
num_stuck = 0

for pos,_ in enumerate(coordinates[0]):
    if coordinates[0][pos] == guard_start_row and coordinates[1][pos] == guard_start_column:
        continue
    else:

        path_string = ''
        path_dict = {}
        test_matrix = copy.deepcopy(matrix_clear)
        test_matrix[coordinates[0][pos],coordinates[1][pos]] = '#'
        guard_row = guard_start_row
        guard_column = guard_start_column
        direction = guard_start_direction
        while guard_row >= 0:
            test_matrix, path_string, direction, guard_row, guard_column, stuck = make_step(test_matrix, direction, guard_row, guard_column)
        if stuck:
            num_stuck +=1

print(num_stuck)

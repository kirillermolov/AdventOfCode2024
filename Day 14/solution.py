#PART 1

max_column = 101
max_row = 103

quadrant_row = (max_row-1)/2
quadrant_column = (max_column-1)/2

quadrants = 4*[0]

def move(row,column,counter,max_counter):
    for i in range(abs(row_velocity)):
       row += row_velocity/abs(row_velocity)
       if row > max_row-1:
           row = 0
       if row < 0:
           row = max_row-1

    for i in range(abs(column_velocity)):
       column += column_velocity/abs(column_velocity)
       if column > max_column-1:
           column = 0
       if column < 0:
           column = max_column-1

    counter += 1
    if counter == max_counter:
        return row, column
    else:
        return move(row,column,counter,max_counter)

def determine_quadrant(row,column):
    if row == quadrant_row or column == quadrant_column:
        return
    if row < quadrant_row:
        i = 0 if column < quadrant_column else 1
    else:
        i = 2 if column < quadrant_column else 3

    quadrants[i] += 1

with open('input.txt') as file:
    for i in file:
       coordinates_part = i.split()[0]
       velocity_part = i.split()[1]

       column = int(coordinates_part[coordinates_part.find("=")+1:].split(',')[0])
       row = int(coordinates_part[coordinates_part.find("=")+1:].split(',')[1])

       column_velocity = int(velocity_part[velocity_part.find("=")+1:].split(',')[0])
       row_velocity = int(velocity_part[velocity_part.find("=")+1:].split(',')[1].strip())
       row, column = move(row,column,0,100)

       determine_quadrant(row,column)

print(quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3])


#PART 2

#The guess behind solution is that picture of christmas tree should have a lot of horizontally symmetric points (have same distance to some column)

from collections import deque
from collections import Counter
import numpy as np

def read_input():
    row_deque = deque()
    column_deque = deque()
    row_velocity_deque = deque()
    column_velocity_deque = deque()
    row_symmetric_deque = deque()
    column_symmetric_deque = deque()
    with open('input.txt') as file:
        for i in file:
            coordinates_part = i.split()[0]
            velocity_part = i.split()[1]

            column = int(coordinates_part[coordinates_part.find("=")+1:].split(',')[0])
            row = int(coordinates_part[coordinates_part.find("=")+1:].split(',')[1])

            column_velocity = int(velocity_part[velocity_part.find("=")+1:].split(',')[0])
            row_velocity = int(velocity_part[velocity_part.find("=")+1:].split(',')[1].strip())

            row_deque.append(row)
            column_deque.append(column)
            row_velocity_deque.append(row_velocity)
            column_velocity_deque.append(column_velocity)

    return row_deque, column_deque, row_velocity_deque, column_velocity_deque

def move(row,column,row_velocity,column_velocity):
    for i in range(abs(row_velocity)):
       row += row_velocity/abs(row_velocity)
       if row > max_row-1:
           row = 0
       if row < 0:
           row = max_row-1

    for i in range(abs(column_velocity)):
       column += column_velocity/abs(column_velocity)
       if column > max_column-1:
           column = 0
       if column < 0:
           column = max_column-1

    return row,column


def check_symmetry_column(column):
    column_symmetric = 0
    for position in robots_position.keys():
        if position.imag < column:
            if robots_position[complex(position.real,column+(column-position.imag))]:
                column_symmetric += 1

    return column_symmetric


def visualize():
    for row in range(max_row):
        string = ''
        for column in range(max_column):
            if robots_position[complex(row,column)] > 0:
                string += '1'
            else:
                string += '.'
        print(string)



row_deque, column_deque, row_velocity_deque, column_velocity_deque = read_input()
column_symmetric_deque = deque()

for time in range(10000):
    robots_position = Counter()
    column_symmetric_max = 0
    for pos,_ in enumerate(row_deque):
        row,column = move(row_deque[pos],column_deque[pos],row_velocity_deque[pos],column_velocity_deque[pos])
        row_deque[pos] = row
        column_deque[pos] = column
        robots_position[complex(row,column)] += 1

    for column in range(1,max_column):
       column_symmetric = check_symmetry_column(column)
       if column_symmetric > column_symmetric_max:
           column_symmetric_max = column_symmetric

    column_symmetric_deque.append(column_symmetric_max)

print(f"Max of horizontally symmetric point achieved after {np.argsort(-np.array(column_symmetric_deque))[0]+1} seconds passed")
print(f"Position of robots after {np.argsort(-np.array(column_symmetric_deque))[0]+1} seconds")
row_deque, column_deque, row_velocity_deque, column_velocity_deque = read_input()
for time in range(np.argsort(-np.array(column_symmetric_deque))[0]+1):
    robots_position = Counter()
    for pos,_ in enumerate(row_deque):
        row,column = move(row_deque[pos],column_deque[pos],row_velocity_deque[pos],column_velocity_deque[pos])
        row_deque[pos] = row
        column_deque[pos] = column
        robots_position[complex(row,column)] += 1

visualize()

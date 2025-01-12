#PART 1
import numpy as np
from itertools import product

def create_matrix_from_file(file_name):
    matrix = []
    matrix_reverse = []
    with open(file_name,'r') as file:
        for i in file:
           row = [char for char in i if char != '\n']
           matrix.append(row)

    return np.array(matrix)

def check_coordinates_valid(x_coordinate,y_coordinate):
    if x_coordinate >= 0 and y_coordinate >= 0 and x_coordinate < column and y_coordinate < row and float(x_coordinate).is_integer() and float(y_coordinate).is_integer():
        return (x_coordinate,y_coordinate)
    return None

def check_att(row_pairs,column_pairs):
    result = set()
    for rows, columns in zip(row_pairs,column_pairs):
        if rows[0] == rows[1] and columns[0] == columns[0]:
            continue
        else:
            if rows[0] == rows[1]:
                result.add(check_coordinates_valid(rows[0], columns[0]+(columns[0]-columns[1])))
            elif columns[0] == columns[1]:
                result.add(check_coordinates_valid(rows[0]+(rows[0]-rows[1]), columns[0]))
            else:
                coeff = (rows[0]-rows[1])/(columns[0]-columns[1])
                new_row = rows[0]+(rows[0]-rows[1])
                new_column = (new_row-rows[0])/coeff+columns[0]
                result.add(check_coordinates_valid(new_row, new_column))
    return result

matrix = create_matrix_from_file('input.txt')
matrix = matrix[::-1]

row = np.shape(matrix)[0]
column = np.shape(matrix)[1]

summa = 0
final_set = set()
for i in np.unique(matrix):
    if i == '.':
        continue

    row_pairs = list(product(np.where(matrix == i)[0], np.where(matrix == i)[0]))
    column_pairs = list(product(np.where(matrix == i)[1], np.where(matrix == i)[1]))
    result = check_att(row_pairs,column_pairs)
    for item in result:
        if item:
           final_set.add(item)

print(len(final_set))

#PART 2

def check_att(row_pairs,column_pairs):
    result = set()
    for rows, columns in zip(row_pairs,column_pairs):
        if rows[0] == rows[1] and columns[0] == columns[0]:
            continue
        else:
            if rows[0] == rows[1]:
                for c in range(0,column):
                    result.add((rows[0], c))
            elif columns[0] == columns[1]:
                for r in range(0, row):
                    result.add((r, columns[0]))
            else:
                coeff = (rows[0]-rows[1])/(columns[0]-columns[1])
                for r in range(0, row):
                    new_column = (r-rows[0])/coeff+columns[0]

                    result.add(check_coordinates_valid(r, new_column))
    return result

summa = 0
final_set = set()
for i in np.unique(matrix):
    if i == '.':
        continue

    row_pairs = list(product(np.where(matrix == i)[0], np.where(matrix == i)[0]))
    column_pairs = list(product(np.where(matrix == i)[1], np.where(matrix == i)[1]))
    result = check_att(row_pairs,column_pairs)
    for item in result:
        if item:
           final_set.add(item)

print(len(final_set))

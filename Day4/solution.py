#PART 1

import re
import numpy as np

pattern = 'XMAS'

def create_matrix_from_file(file_name):
    matrix = []
    matrix_reverse = []
    with open(file_name,'r') as file:
        for i in file:
           row = [char for char in i if char != '\n']
           matrix.append(row)
           matrix_reverse.insert(0,row)
    return np.array(matrix), np.array(matrix_reverse)

def reverse_string(line):
    reversed_string = ''
    for i in range(len(line)-1, -1, -1):
        reversed_string += line[i]
    return reversed_string

def get_all_horizontal_lines(matrix, counter):
     for i in range(0,np.shape(matrix)[0]):
        counter += len(re.findall(pattern, "".join(matrix[i,:])))
        counter += len(re.findall(pattern, reverse_string("".join(matrix[i,:]))))
     return counter

def get_all_vertical_lines(matrix, counter):
    for i in range(0,np.shape(matrix)[1]):
        counter += len(re.findall(pattern, "".join(matrix[:,i])))
        counter += len(re.findall(pattern, reverse_string("".join(matrix[:,i]))))
    return counter

def get_all_diagonal_lines(matrix,matrix_reverse,counter):
    for diag in range(-(np.shape(matrix)[0]-4), np.shape(matrix)[0]-3):
        counter += len(re.findall(pattern, "".join(np.diag(matrix, diag))))
        counter += len(re.findall(pattern, reverse_string("".join(np.diag(matrix, diag)))))
    for diag in range(-(np.shape(matrix_reverse)[0]-4), np.shape(matrix_reverse)[0]-3):
        counter += len(re.findall(pattern, "".join(np.diag(matrix_reverse, diag))))
        counter += len(re.findall(pattern, reverse_string("".join(np.diag(matrix_reverse, diag)))))

    return counter


counter = 0
matrix, matrix_reverse = create_matrix_from_file('input.txt')
counter = get_all_horizontal_lines(matrix, counter)
counter = get_all_vertical_lines(matrix, counter)
counter = get_all_diagonal_lines(matrix, matrix_reverse, counter)
print(counter)

#PART 2

def apply_mask(input_part):
    if np.shape(input_part) != (3,3):
        return False
    else:
        if (np.diag(input_part, 0) == ['M','A','S']).all() or (np.diag(input_part, 0) == ['S','A','M']).all():
          if (input_part[2,0] == 'M' and input_part[0,2] == 'S') or (input_part[2,0] == 'S' and input_part[0,2] == 'M'):
              return True
        return False

counter = 0
matrix, _ = create_matrix_from_file('input.txt')

for i in range(0, np.shape(matrix)[0]):
    for j in range(0, np.shape(matrix)[1]):
       if apply_mask(matrix[i:i+3,j:j+3]):
           counter += 1

print(counter)

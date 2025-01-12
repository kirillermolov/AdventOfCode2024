#PART 1

import numpy as np

def check_order(array):
    if (np.sort(array) == array).all():
        return True
    if (-np.sort(-array) == array).all():
        return True
    return False

def check_difference(array):
    difference_list = [np.abs(array[i]-array[i+1]) for i in range(0,len(array)-1)]
    if np.max(difference_list) > 3 or np.min(difference_list) < 1:
        return False
    else:
        return True

safe_counter = 0
with open('input_file.txt') as file:
    for line in file:
        array = np.array(line.split(),dtype = np.int32)
        if check_order(array):
            if check_difference(array):
                safe_counter += 1

print(safe_counter)

#PART 2

def check_order(array):
    if (np.sort(array) == array).all():
        return True
    if (-np.sort(-array) == array).all():
        return True
    return False

def dampener_check(array):
    for i in range (0,len(array)):
        if check_order(np.delete(array, [i])):
            if check_difference(np.delete(array, [i])):
                return True
    return False

def check_difference(array):
    difference_list = [np.abs(array[i]-array[i+1]) for i in range(0,len(array)-1)]
    if np.max(difference_list) > 3 or np.min(difference_list) < 1:
        return False
    else:
        return True

def difference_dampener(array):
    difference_list = np.array([np.abs(array[i]-array[i+1]) for i in range(0,len(array)-1)])
    bad_index = np.where((difference_list > 3) | (difference_list == 0))[0]
    if len(bad_index) > 1:
        return False
    else:
        if check_difference(np.delete(array, bad_index)) or check_difference(np.delete(array, bad_index+1)):
            return True
    return False

safe_counter = 0
with open('input_file.txt') as file:
    for line in file:
        array = np.array(line.split(),dtype = np.int32)
        if check_order(array) and check_difference(array):
                safe_counter += 1
        else:
            if dampener_check(array):
                    safe_counter += 1

print(safe_counter)

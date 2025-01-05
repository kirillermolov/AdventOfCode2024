#PART 1

import math

with open('input.txt', 'r') as file:
    rules_dict = {}
    middle_sum = 0
    for line in file:
        line = line.replace('\n', '')
        if '|' in line:
            line = line.split('|')
            if line[0] in rules_dict.keys():
                rules_dict[line[0]].append(line[1])
            else:
                rules_dict[line[0]] = [line[1]]


        if ',' in line:
            splitted_line = line.split(',')
            middle = int(splitted_line[math.floor(len(splitted_line)/2)])
            outer_loop = True
            for i in (splitted_line):
                for ii in rules_dict.get(i,[]):
                    try:
                        if splitted_line.index(i) > splitted_line.index(ii):
                            outer_loop = False
                            break
                    except:
                        pass
                if not outer_loop:
                    break

            if outer_loop:

                middle_sum += middle

print(middle_sum)


#PART 2

def check_wrong_pairs(splitted_line,rules_dict):
    for i in (splitted_line):
        for ii in rules_dict.get(i,[]):
            try:
                if splitted_line.index(i) > splitted_line.index(ii):
                    return splitted_line.index(i), splitted_line.index(ii)
            except:
                pass
    return None, None

with open('input.txt', 'r') as file:
    rules_dict = {}
    middle_sum = 0
    middle_incorrect_sum = 0
    for line in file:
        line = line.replace('\n', '')
        if '|' in line:
            line = line.split('|')
            if line[0] in rules_dict.keys():
                rules_dict[line[0]].append(line[1])
            else:
                rules_dict[line[0]] = [line[1]]


        if ',' in line:
            splitted_line = line.split(',')
            middle = int(splitted_line[math.floor(len(splitted_line)/2)])
            outer_loop = True
            for i in (splitted_line):
                for ii in rules_dict.get(i,[]):
                    try:
                        if splitted_line.index(i) > splitted_line.index(ii):
                            outer_loop = False
                            break
                    except:
                        pass
                if not outer_loop:
                    break

            if not outer_loop:
                index1 = 1
                while index1:
                    index1, index2 = check_wrong_pairs(splitted_line,rules_dict)
                    if index1:
                        value_index1 = splitted_line[index1]
                        value_index2 = splitted_line[index2]
                        splitted_line[index1] = value_index2
                        splitted_line[index2] = value_index1
                middle = int(splitted_line[math.floor(len(splitted_line)/2)])
                #print(splitted_line)
                middle_incorrect_sum += middle

print(middle_incorrect_sum)

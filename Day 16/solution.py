#PART 1

from collections import defaultdict

direction_dict = {}

def parse_input(path):
    with open(path, "r") as input:
        return {
            complex(row_ix, col_ix): char
            for row_ix, row in enumerate(input)
            for col_ix, char in enumerate(row.strip())
        }

position_dictionary = parse_input('input.txt')

end_position = None
start_position = None
for pos, char in position_dictionary.items():
    if char == 'E':
        end_position = pos
    if char == 'S':
        start_position = pos
    if end_position and start_position:
        break
direction_list = [1,-1,complex(0,1),complex(0,-1)]
position_score = defaultdict(lambda: defaultdict(int))

def calculate_score(income_direction, position):
    for direction in direction_list:
        if direction == -income_direction:
            continue
        if position_dictionary[position+direction] != '#':
            pos_score = position_score[position][income_direction] + 1
            if direction != income_direction:
                pos_score += 1000
            if position_score[position+direction][direction] == 0 or pos_score < position_score[position+direction][direction]:
                position_score[position+direction][direction] = pos_score
                list_to_process.append((direction, position+direction))
                return True

list_to_process = []
if position_dictionary[start_position-1] != '#':
    position_score[start_position-1][-1] = 1+1000
    list_to_process.append((-1, start_position-1))
    to_continue = True
    while to_continue:
        to_continue = False
        for item in list_to_process:
            if calculate_score(item[0],item[1]):
                to_continue = True

list_to_process = []
if position_dictionary[start_position+complex(0,1)] != '#':
    position_score[start_position+complex(0,1)][complex(0,1)] = 1
    list_to_process.append((complex(0,1), start_position+complex(0,1)))
    to_continue = True
    while to_continue:
        to_continue = False
        for item in list_to_process:
            if calculate_score(item[0],item[1]):
                to_continue = True

print(min(position_score[end_position].values()))

#PART 2

optimal_positions = set()

optimal_positions.add(end_position)
optimal_positions.add(start_position)

def check_if_optimal(position,optimal_value):
    opt_value1 = optimal_value - 1001
    opt_value2 = optimal_value - 1
    for direction in direction_list:
        if opt_value1 in position_score[position+direction].values():
            optimal_positions.add(position+direction)
            check_if_optimal(position+direction, opt_value1)

        if opt_value2 in position_score[position+direction].values():
            optimal_positions.add(position+direction)
            check_if_optimal(position+direction, opt_value2)


check_if_optimal(end_position,min(position_score[end_position].values()))
print(len(optimal_positions))

#PART 1

def parse_input(path):
    with open(path, "r") as input:
        return {
            complex(row_ix, col_ix): char
            for row_ix, row in enumerate(input)
            for col_ix, char in enumerate(row.strip())
        }


position_dictionary = parse_input('input.txt')
direction_list = [1,-1,complex(0,1),complex(0,-1)]

def check_border(coordinate):
    border = 0
    for direction in direction_list:
        try:
           if position_dictionary[coordinate+direction] != position_dictionary[coordinate]:
               border += 1
        except:
            border += 1
    return border



def move(coordinate,direction):
    global border_total
    try:
        if position_dictionary[coordinate+direction] == position_dictionary[coordinate]:
            if coordinate+direction not in processed_coordinate:
                border_total += check_border(coordinate+direction)
                processed_coordinate.add(coordinate+direction)
            else:
                return
        else:
            return

    except:
        return

    coordinate = coordinate+direction
    for direction in direction_list:
        move(coordinate,direction)


processed_coordinate_global = set()
result = 0
for coordinate in position_dictionary.keys():
    if coordinate not in processed_coordinate_global:
            processed_coordinate ={coordinate}
            border_total = check_border(coordinate)
            for direction in direction_list:
                move(coordinate,direction)
            result += border_total*len(processed_coordinate)

    if processed_coordinate_global:
       processed_coordinate_global.update(processed_coordinate)
    else:
        processed_coordinate_global = processed_coordinate

print(result)

#PART 2

def check_border(coordinate):
    for direction in direction_list:
        try:
           if position_dictionary[coordinate+direction] != position_dictionary[coordinate]:
               border_set.add((coordinate,direction))
        except:
            border_set.add((coordinate,direction))

def move_border(border_coordinate, border_direction, direction, call_number):
    global bulk
    if border_direction != direction:
        return

    if isinstance(direction, complex):
        check_direction = -1
        move_direction = 1

    else:
        check_direction = complex(0,-1)
        move_direction = complex(0,1)
    if (border_coordinate+check_direction, direction) in border_set and call_number == 0:
        return
    if (border_coordinate+move_direction, direction) in border_set:
        move_border(border_coordinate+move_direction, border_direction, direction, call_number+1)
    else:
        bulk += 1
        return

def move(coordinate,direction):
    try:
        if position_dictionary[coordinate+direction] == position_dictionary[coordinate]:
            if coordinate+direction not in processed_coordinate:
                check_border(coordinate+direction)
                processed_coordinate.add(coordinate+direction)
            else:
                return
        else:
            return

    except:
        return

    coordinate = coordinate+direction
    for direction in direction_list:
        move(coordinate,direction)


processed_coordinate_global = set()
result = 0
for coordinate in position_dictionary.keys():
    if coordinate not in processed_coordinate_global:
            processed_coordinate ={coordinate}
            border_set = set()
            processed_border = set()
            check_border(coordinate)
            for direction in direction_list:
                move(coordinate,direction)
            bulk = 0
            for border_position in border_set:
                for direction in direction_list:
                    move_border(border_position[0],border_position[1], direction, 0)

            result += bulk*len(processed_coordinate)

    if processed_coordinate_global:
       processed_coordinate_global.update(processed_coordinate)
    else:
        processed_coordinate_global = processed_coordinate


print(result)

#PART 1

def generate_string(original_string):
    new_string = ''
    for pos, char in enumerate(original_string):
        if pos%2 == 0:
            new_string += int(char)*((str( int(pos/2) ) ) + " ")
        else:
            new_string += int(char)*'. '
    return new_string.split()

with open('input.txt') as file:
    new_string = generate_string(file.read().strip())

i = len(new_string)-1
empty = 0
while i > empty:
     if new_string[i] != '.':
         empty = new_string.index('.',empty)
         new_string[empty] = new_string[i]
         new_string[i] = '.'
         empty+=1
     i -= 1


summa = 0
for pos, value in enumerate(new_string):
    if value == '.':
        break
    summa += pos*int(value)

print(summa)

#PART 2

import numpy as np

def generate_string(original_string):
    new_string = []
    for pos, char in enumerate(original_string):
        if pos%2 == 0:
            new_string.append( (int(char)*((str( int(pos/2) ) ) + " ") ).strip() )
        else:
            new_string.append((int(char)*'. ').strip())
    return np.array(new_string,dtype=object)

with open('input.txt') as file:
    new_string = generate_string(file.read().strip())

len_new_string = np.array(list(map(lambda element: len(element.split()), new_string)))

failed_length = max(len_new_string)+1
i = len(len_new_string)-1

while i > 0:
    #print("call")
    if '.' not in new_string[i] and len_new_string[i] != 0:
      if len_new_string[i] < failed_length:
          suitable_list = np.where(len_new_string[0:i] >= len_new_string[i])[0]
          suitable_index = None
          for suit in suitable_list:
              if '.' in new_string[suit]:
                  suitable_index = suit
                  break
          if suitable_index is not None:
              #new_string[suitable_index] = new_string[suitable_index] + " " + new_string[i]
              indexes_to_change = []
              string_list = new_string[suitable_index].split()
              for ind in range(0,len_new_string[i]):
                  string_list[string_list.index('.')] = new_string[i].split()[0]
                  new_string[suitable_index] = " ".join(string_list)

              len_new_string[suitable_index] -= len_new_string[i]
              new_string[i] = '. '*len_new_string[i]
          else:
              failed_length = len_new_string[i]


    i -= 1

summa = 0
pos = 0

for element in new_string:
    for i in element.split():
        if i != '.':
            summa += pos*int(i)
        pos+=1

print(summa)

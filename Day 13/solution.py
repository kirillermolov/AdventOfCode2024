#PART 1

from scipy.linalg import solve

A = []
b = []
summa = 0
with open('input.txt') as file:
    for line in file:
        if line.strip():
            if 'Button' in line.split(':')[0]:
                button = True
            else:
                button = False

            number_values = line.split(':')[1].split(',')
            if button == True:
                A.append([int(number_values[0][number_values[0].find('+')+1:].strip()), int(number_values[1][number_values[1].find('+')+1:].strip())])
            else:
                b.append([int(number_values[0][number_values[0].find('=')+1:].strip())])
                b.append([int(number_values[1][number_values[1].find('=')+1:].strip())])
                A_transpose = [[row[i] for row in A] for i in range(len(A[0]))]
                try:
                    correct = True
                    x = solve(A_transpose,b)
                    for solution in x:
                        stabil_solution = float("{:.3f}".format(solution[0]))
                        if stabil_solution > 100 or stabil_solution.is_integer() == False:
                          correct = False
                    if correct:
                        summa += 3*x[0][0]+x[1][0]
                    A = []
                    b = []
                except:
                     A = []
                     b = []
                     
print(f"{summa:.0f}")

#PART 2

A = []
b = []
summa = 0
with open('input.txt') as file:
    for line in file:
        if line.strip():
            if 'Button' in line.split(':')[0]:
                button = True
            else:
                button = False

            number_values = line.split(':')[1].split(',')
            if button == True:
                A.append([int(number_values[0][number_values[0].find('+')+1:].strip()), int(number_values[1][number_values[1].find('+')+1:].strip())])
            else:
                    b.append([int('10000000000000')+int(number_values[0][number_values[0].find('=')+1:].strip())])
                    b.append([int('10000000000000')+int(number_values[1][number_values[1].find('=')+1:].strip())])
                    A_transpose = [[row[i] for row in A] for i in range(len(A[0]))]
                    correct = True
                    x = solve(A_transpose,b)

                    for solution in x:
                        stabil_solution = float("{:.3f}".format(solution[0]))
                        if stabil_solution.is_integer() == False:
                          correct = False
                    if correct:
                        summa += 3*x[0][0]+x[1][0]
                    A = []
                    b = []

print(f"{summa:.0f}")

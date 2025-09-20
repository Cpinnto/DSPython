# List review (Python)
lst = ["Carlos", 31, "HCC"]
print(lst)

matrix = [[1,2,3],[4,5,6]]

matrix1 = [[0,0,0],[0,0,0]]

for i in range(10):
    lst.append(i)
for row in range(2):
    for col in range(3):
        matrix[row][col] = row + col 

# Use list comprehesion 

import random
one_dim = [random.randint(1,100) for _ in range(5)] # _ Significa la variable temporal que va a guardar el numero generado a la zar, range(5) generara 5 numeros a l azar

# print(f'one_dim = {on p\'/e_dim}')

two_dim = [[random.randint(1,100) for _ in range(5)] for _ in range(3)] # basicamente, for _ in range(3) genera 3 row, basicamente _ es la variable tempora usada para el numero generado dentro del loop
print(f'two_dimension = {two_dim}')


# List traversing
# 1. using index 
for i in range(len(one_dim)):
    print(one_dim[i], end=' ')
print()

# 2. Using collection wat

for num in one_dim:
    print(num, end=" ")
print()


# Traversing two dim

for row in range(len(two_dim)):
    for col in range(len(two_dim[row])):
        print(f'{two_dim[row][col]}:3d', end=' ')
print()


# Locate the max value
max_one_dim = max(one_dim)
print(f'Max value = {max_one_dim}')

# Two-dim 
    # 1.
max_row = [max(row) for row in two_dim] # va a generar un lista, pero pondra el numero mas alto de cada row
max_two_dim = max(max_row)
print(f'Max in two_dim: {max_two_dim}')


# Flatten the two dim
# flatten_list = [num for row i two_dim for num in row]
# print('max falue in flatten list:', max(flatten_list))

# List slicing
lst = [3, 10, 45, 6, 7, 34, 5]
print(lst)
print(lst[-3:-5:-1])
print(lst[::-1])  # Esto hara invertira la lista, esto se mirara Nympy 



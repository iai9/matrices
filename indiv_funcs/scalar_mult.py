'''
imran
11-7-21

multiply a TWO DIMENSIONAL array in form of:

    array = [
        [a1, a2, a3, ..., aN],
        [b1, b2, b3, ..., bN],
        [c1, c2, c3, ..., cN],
        ...,
        [z1, z2, z3, ..., zN],
    ]

with a scalar. 

log.txt separate

known bugs:
    no known bugs as of now

'''

######### Dependencies

''' none'''

######### Funcs

def matrix_by_scalar(matrix1, scalar_quantity):

    if (isinstance(scalar_quantity, int)) or (isinstance(scalar_quantity, float)):

        return  list([element * scalar_quantity for element in row] \
                for row in matrix1) # O(n**2)
    
    else: raise ValueError(f"Argument passed: '{scalar_quantity}'. Error: Expected argument of type 'int' or 'float' ")

######### Vars

m1 = [
    [3,6],
    [1,4],
    [9,8]
]

num = 4.56

######### Main

print(matrix_by_scalar(m1, num))
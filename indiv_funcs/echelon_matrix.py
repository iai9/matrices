'''
11-9-21
imran iftikar

the purpose of this program is to take a given SQAURE TWO DIMENSIONAL matrix in the form :

    array = [
    [a1, a2, a3, ..., aN],
    [b1, b2, b3, ..., bN],
    [c1, c2, c3, ..., cN],
    ...,
    [z1, z2, z3, ..., zN],
    ]

and find its echelon, upper triangle form
this is useful for finding its determinant
I also forsee myself using this code to find the inverse of a matrix larger than 2x2, by using an identity matrix and eliminating from there

log.txt separate

known bugs:
    none 



'''

######### Dependencies

'''none'''

######### Functions


def get_col(matrix_2d, _index):
    return list(row[_index] for row in matrix_2d) # O(n)

def row_by_scalar(row, scalar_quantity):

    if (isinstance(scalar_quantity, int)) or (isinstance(scalar_quantity, float)):
        return list((element*scalar_quantity) for element in row)
    
    else: raise ValueError("u r returardedd lamo")

def sub_row(row1, row2):

    if len(row1) == len(row2):
        
        return list((row1[i] - row2[i]) for i in range(len(row1)))

    else:
        raise ValueError("Rows are different sizes and cannot be subtracted")

def echelon(matrix):

    if (len(matrix)) == (len(matrix[0])): #O(1)
        
        for col_index in range(len(matrix[0])): #O(n)
            col = get_col(matrix, col_index) # O(n)
            for row_index in range(len(col)): # O(n)

                if row_index <= col_index: #O(1)
                    if row_index == col_index: #O(1)
                        denominator = matrix[row_index][col_index] #O(1)
                        raw_subtractant_row = matrix[row_index] #O(1)
                    pass              

                else:
                    row_to_sub_from = matrix[row_index] # O(1)
                    numerator = matrix[row_index][col_index] #O(1)


                    subtractant = row_by_scalar(raw_subtractant_row, (numerator/denominator)) # O(n)
                    subbed_row = sub_row(row_to_sub_from, subtractant) # O(1)

                    matrix[row_index] = subbed_row
        
        return matrix

    else:
        raise ValueError("List is not sqaure")

######### Vars

m1 = [
        [27,5,6],
        [4,6,2],
        [5,2,6]
]

######### Main

print(echelon(m1))


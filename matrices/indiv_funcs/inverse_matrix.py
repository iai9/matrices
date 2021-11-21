'''
imran iftikar
11.19.21

finds the inverse of a matrix by using reduction and a secondary identity matrixS


'''

######### Dependencies


from echelon_matrix import echelon
from transpose_matrix import transpose
from reflect_matrix import reflect

######### Funcs

def make_identity(dim):

    l = []

    for one_idx in range(dim):
        new_row = [0 for i in range(dim)]
        new_row[one_idx] = 1
        l.append(new_row)
    
    return l

def get_col(matrix_2d, _index):
    return list(row[_index] for row in matrix_2d) # O(n)

def row_by_scalar(row, scalar_quantity):

    if (isinstance(scalar_quantity, int)) or (isinstance(scalar_quantity, float)):
        return list((element*scalar_quantity) for element in row)
    
    else: raise ValueError(" cannot multiply row by non-integer or non-float value")

def subtract_row(row1, row2):

    if len(row1) == len(row2):
        
        return list((row1[i] - row2[i]) for i in range(len(row1)))

    else:
        raise ValueError("Rows are different sizes and cannot be subtracted")


def inverse(matrix): #

    identity = make_identity(len(matrix))

    for i in range(0,2):
        
        for col_index in range(len(matrix[0])): #O(n) this first for loop handles zeroes that might potentially lead to div by 0 errors
            col = get_col(matrix, col_index) # O(n)

            if col_index <= len(matrix): # O(1)

                if all((i == 0) for i in col[col_index:]): #O(n)
                    continue 
                
                elif col[col_index] == 0: # O(1)
                    for i in range(len(col[col_index:])): #O(n)
                        if col[col_index:][i] != 0: # O(1)
                            row_idx = col_index+i # O(1)
                            break 
                    
                    matrix[col_index], matrix[row_idx] = matrix[row_idx], matrix[col_index] # O(n)


            for row_index in range(len(col)): # O(n)

                if row_index <= col_index: #O(1)
                    if row_index == col_index: #O(1)
                        denominator = matrix[row_index][col_index] #O(1)
                        raw_subtractant_row = matrix[row_index] #O(1)
                        raw_subtractant_row_identity = identity[row_index]
                    pass              

                else:

                    numerator = matrix[row_index][col_index] #O(1)

                    row_to_sub_from = matrix[row_index] # O(1)
                    subtractant = row_by_scalar(raw_subtractant_row, (numerator/denominator)) # O(n)
                    subbed_row = subtract_row(row_to_sub_from, subtractant) # O(1)
                    matrix[row_index] = subbed_row


                    subtractant_identity = row_by_scalar(raw_subtractant_row_identity, (numerator/denominator))
                    subbed_row1 = subtract_row(identity[row_index], subtractant_identity)
                    identity[row_index] = subbed_row1  
        
        matrix = reflect(matrix)
        identity = reflect(identity)
    
    print(matrix)
    print(identity)

    for i in range(len(matrix)):
        identity[i] = row_by_scalar(identity[i], (1/matrix[i][i]))
    
    print(identity)



######### Vars

######### Main

# print(make_identity(5))
 

test = [
    [2,6,2],
    [2,7,1],
    [5,6,1]

]



print(inverse(test))
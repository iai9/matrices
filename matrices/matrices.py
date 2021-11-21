'''
imran iftikar
11.20.21

This file is a compilation file - essentially a "library" of all of the matrix functions I have written
For information on each individual file, consult "./indiv_funcs/", a directory containing each individual file as i wrote them
In the future, that will likely not be maintained.

In general, this "library" is to be used with TWO DIMENSIONAL arrays in the form:

    array = [
        [a1, a2, a3, ..., aN],
        [b1, b2, b3, ..., bN],
        [c1, c2, c3, ..., cN],
        ...,
        [z1, z2, z3, ..., zN],
    ]

currently, there is support for:
*   Multiplication by scalar
*   Mutliplication of matrices
*   Addition of matrices
*   subtraction of matrices
*   tranpose
*   echelon
*   determinants
*   inverse

I have made an effort to provide good documentation. Where I felt it was necessary, I included time complexity of code

log.txt separate

known bugs:    
    none

'''

######### Dependencies

''' none '''

######### Main

def matrix_by_scalar(matrix1, scalar_quantity):

    if (isinstance(scalar_quantity, int)) or (isinstance(scalar_quantity, float)): # O(1) checks if the second arg is valid

        return  list([element * scalar_quantity for element in row] \
                for row in matrix1) # O(n**2) Multiplies each element of each row by the scalar and thus has a time complexity of n**2
    
    else: raise ValueError(f"Argument passed: '{scalar_quantity}'. Error: Expected argument of type 'int' or 'float' ") # error raised

    # full time O(n**2)

def add_matrices(mat1, mat2): 

    if (len(mat1) == (len(mat2)) and (len(mat1[0]) == len(mat2[0]))): # check to see if possible to add the two lists. constant time i think

        # the following is a rather long list comprehension. it just adds each row and col of the two lists together
        # basically just two for loops
        l = list([mat1[row][col]+mat2[row][col] \
            for col in range(len(mat1[0]))] \
            for row in range(len(mat1))) # O(n**2)
        return l
    
    else:
        raise ValueError("Args are different size and thus cannot be added")
    
    # full time O(n**2)

def subtract_matrices(mat1, mat2): # subtracts second term from first

    if (len(mat1) == (len(mat2)) and (len(mat1[0]) == len(mat2[0]))): # check to see if possible to add the two lists. constant time i think

        # the following is a rather long list comprehension. it just adds each row and col of the two lists together
        # basically just two for loops
        l = list([mat1[row][col]-mat2[row][col] \
            for col in range(len(mat1[0]))] \
            for row in range(len(mat1))) # O(n**2)
        return l

    else:
        raise ValueError("Args are different size and thus cannot be subtraction")
    
    # full time, O(n**2)

def get_col(matrix_2d, _index):

    return list(row[_index] for row in matrix_2d) # O(n) this simply grabs the column from the specified index. 

    # full time O(n)

def transpose(matrix):

    new_array = [get_col(matrix, i) for i in range(len(matrix[0]))] # O(n) and nested O(n), becomes O(n**2). takes a column and makes it a row
    return new_array

    # full time O(n**2)

def row_by_scalar(row, scalar_quantity):

    # the functionality of this function is used in the echelon and inverse function.

    if (isinstance(scalar_quantity, int)) or (isinstance(scalar_quantity, float)): # checks if argument 2 is valid
        return list((element*scalar_quantity) for element in row) # simple list comprehension. linear time, O(n)
    
    else: raise ValueError(" cannot multiply row by non-integer or non-float value") # raises erorr if arg2 is invalid

    # full time O(n)

def subtract_row(row1, row2):

    # this is used in echelon and inverse

    if len(row1) == len(row2): # makes sure that args can be subtracted
        
        return list((row1[i] - row2[i]) for i in range(len(row1))) # list comprehension with linear time, O(n)

    else:
        raise ValueError("Rows are different sizes and cannot be subtracted") # raises error is size of rows is different

    # full time O(n)

def echelon(matrix): 
    
    for col_index in range(len(matrix[0])): # Indiv O(n), Overall (n**3) the formula I devised uses columns, so I start with that. 
        
        col = get_col(matrix, col_index) # O(n) we grab the column using the index from the above for loop

        '''
        
        the following bit of code looks for places where there might be zeroes in the diagonal.
        if there are, and we do not handle for it, we get a dividing by zero error

        thus, the following code is quite necessary.  
        
        '''
        if col_index <= len(matrix): # O(1) we only need to look for zeroes in the first square - that is, if the matrix is longer than tall, it is uncessary to check all columns

            if all((i == 0) for i in col[col_index:]): #O(n) if the entire column is filled with zeroes, we call continue and the program returns to the initial for loop, and goes to the next column
                continue 
            
            elif col[col_index] == 0: # O(1) if one of the elements on the diagonal is zero - this is where the dividing by zero error occurs so we need to handle this
                ''' 
                here we iterate through all of the rows below the diagonal. 
                if we find a row that doesn't contain a zero in the diagonal column index, 
                we will swap them
                '''
                for i in range(len(col[col_index:])): #O(n) 
                    if col[col_index:][i] != 0: # O(1)
                        row_idx = col_index+i # O(1)
                        break 
                
                # the below line of code simple swaps the rows
                matrix[col_index], matrix[row_idx] = matrix[row_idx], matrix[col_index] # O(1)


        '''
        the following for loop is where the actual formula happens
        the algorithm works as follows:

        assume we have an array

        
        '''
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
                subbed_row = subtract_row(row_to_sub_from, subtractant) # O(1)

                matrix[row_index] = subbed_row # O(1)
    
    return matrix

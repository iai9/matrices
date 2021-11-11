'''
11.10.21
imran a iftikar

the purpose of this program is to find the determinant of TWO DIMENSIONAL matrix IN UPPER TRIANGLE ECHELON FORM

    array = [
            [a1, a2, a3, a4, ..., aN],
            [0, b2, b3, b4, ..., bN],
            [0, 0, c3, c4, ..., cN],
            ...,
            [0, 0, 0, 0, ..., zN]
    ]

i've already made a program to find the echelon form of a matrix, so I don't need to worry about that. 
Here, I will find det by iterating through a list in echelon form


'''

######### Dependencies

'''none'''

######### Funcs

def matrix_det(matrix):

    if len(matrix) == len(matrix[0]):

        det = 1
        for diag_index in range(len(matrix)): # O(n)
            det = det*matrix[diag_index][diag_index]
    
        return det
    
    else:
        print(f"Error: argument expected to be square")

######### Vars

m1 = [[27, 5, 6], [0.0, 5.2592592592592595, 1.1111111111111112], [0.0, 0.0, 4.661971830985916]]

######### Main

print(matrix_det(m1))
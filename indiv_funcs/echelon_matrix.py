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

def echelon(matrix):

    if (len(matrix)) == (len(matrix[0])):
        pass
    else:
        raise ValueError("List is not sqaure")

######### Vars

######### Main


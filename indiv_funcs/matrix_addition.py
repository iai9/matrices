'''
imran iftikar
11-7-21

will add two, TWO DIMENSIONAL matrices in the form:

    array = [
        [a1, a2, a3, ..., aN],
        [b1, b2, b3, ..., bN],
        [c1, c2, c3, ..., cN],
        ...,
        [z1, z2, z3, ..., zN],
    ]


as always, ill try to note down time. 
appending subtraction here because its the same code but literally just one operation changed

log.txt separate

known bugs:
    none
'''

######### Dependencies

''' none'''

######### Funcs

def add_matrices(mat1, mat2): 

    if (len(mat1) == (len(mat2)) and (len(mat1[0]) == len(mat2[0]))): # check to see if possible to add the two lists. constant time i think

        # the following is a rather long list comprehension. it just adds each row and col of the two lists together
        # basically just two for loops
        l = list([mat1[row][col]+mat2[row][col] \
            for col in range(len(mat1[0]))] \
            for row in range(len(mat1))) # O(n**2)
        return l

def subtract_matrices(mat1, mat2): # subtracts second term from first

    if (len(mat1) == (len(mat2)) and (len(mat1[0]) == len(mat2[0]))): # check to see if possible to add the two lists. constant time i think

        # the following is a rather long list comprehension. it just adds each row and col of the two lists together
        # basically just two for loops
        l = list([mat1[row][col]-mat2[row][col] \
            for col in range(len(mat1[0]))] \
            for row in range(len(mat1))) # O(n**2)
        return l


######### Vars

m1 = [
    [3,6],
    [1,4],
    [9,8]
]
m2 = [
    [7,7],
    [5,2],
    [3,1]
]

######### Main

print(add_matrices(m1,m2))
print(subtract_matrices(m1,m2))
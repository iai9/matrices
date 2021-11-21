'''
imran iftikar
11.20.21

this program will reflect a TWO DIMENSIONAL matrix about the secondary diagonal.
thus this is different than transposing
the algorithm I have derived is rather contrived, and thus I will be looking to improve it in the future. 
It works by flipping the matrix, getting its transpose, flipping it again, and finally getting its transpose once again
The problem here is that transpoe gas a time of n**2. 

thus, flip() has a time complexity of n**2
as such, reflect has a time complexity of O(2(2(n**2))) and thus is O(4*n**2) which becomes O(n**2)
this time complexity for such a simple operation is undesirable.

oh well. 

log.txt separate

known bugs:
    none

'''

######### Dependencies

from transpose_matrix import transpose

######### Funcs

def flip(matrix):
    matrix = transpose(matrix) 
    n = len(matrix) 
    holder = [i for i in range(n)]    
    for i in range(0,n): 
        holder[i] = matrix[(n-1-i)]
    return transpose(holder)

def reflect(matrix):
    for i in range(2):
        matrix = flip(matrix)
        matrix = transpose(matrix)
    return matrix


######### Vars

m1 = [
        [1,3,4],
        [1,6,2],
        [9,4,2]
]


######### Main



   






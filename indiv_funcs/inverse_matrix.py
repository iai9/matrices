'''
imran iftikar
11.19.21

finds the inverse of a matrix by using reduction and a secondary identity matrixS


'''

######### Dependencies


from echelon_matrix import echelon
from transpose_matrix import transpose

######### Funcs

def make_identity(dim):

    l = []

    for one_idx in range(dim):
        new_row = [0 for i in range(dim)]
        new_row[one_idx] = 1
        l.append(new_row)
    
    return l



######### Vars

######### Main

print(make_identity(5))
def get_col(matrix_2d, _index):
    return list(row[_index] for row in matrix_2d) # O(n)

def transpose(matrix):

    new_array = [get_col(matrix, i) for i in range(len(matrix[0]))] # O(n) and nested O(n), becomes O(n**2)
    return new_array
   

def fliplr(matrix):
    matrix = transpose(matrix)
    n = len(matrix)
    holder = [i for i in range(n)]    
    for i in range(0,n):
        holder[i] = matrix[(n-1-i)]
    return transpose(holder)

def reflect(matrix):
    for i in range(2):
        matrix = fliplr(matrix)
        matrix = transpose(matrix)
    return matrix

m1 = [
        [1,3],
        [1,6],
]



print(reflect(m1))
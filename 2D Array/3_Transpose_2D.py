
def transpose(matrix):
    m=len(matrix) # Rows
    n=len(matrix[0]) # Cols
    
    return [list(row) for row in zip(*matrix)]
    
    result=[[0]*m for _ in range(n)]
    # return result
    
    for i in range(m):
        for j in range(n):
            result[j][i]=matrix[i][j]
    return result
    
matrix=[[1,2,3], [4,5,6]]
print(transpose(matrix))
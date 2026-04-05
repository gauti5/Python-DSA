# Set Matrix Zeros (leetcode - 73)

def set_matrix_zero(matrix):
    m=len(matrix)
    n=len(matrix[0])
    rows,cols=set(), set()
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                rows.add(i)
                cols.add(j)
    for r in rows:
        for i in range(n):
            matrix[r][i]=0
    for c in cols:
        for j in range(m):
            matrix[j][c]=0
    return matrix
                
    
matrix=[[1,2,4],[1,1,4], [3,2,0]]
print(set_matrix_zero(matrix))
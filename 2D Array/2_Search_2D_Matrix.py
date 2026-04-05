# Search  2D Matrix

def Search_2D(matrix, target):
    
    # Optimal Approach
    rows=len(matrix)
    cols=len(matrix[0])
    
    low=0
    high=(rows*cols)-1
    
    while low<=high:
        mid=(low+high)//2
        row=mid//cols
        col=mid%cols
        middle_value=matrix[row][col]
    
    
        if middle_value==target:
            return True
        elif middle_value<target:
            row=mid+1
        else:
            high=mid-1
            
        
    return False
    
    # Brute Force
    for row in matrix:
        for col in row:
            if target==col:
                return True
    return False

matrix=[[1,2,3,4], [5,6,7,8], [9,1,2,3]]
target=0
print(Search_2D(matrix, target))
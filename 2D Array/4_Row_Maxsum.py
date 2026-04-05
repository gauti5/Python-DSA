# Find a Row with Maximum Sum

def maximum(matrix):
    
    # Optimal 
    max_row, max_sum=max(enumerate(map(sum,matrix)), key=lambda x:x[1])
    print("Maximum Sum :- ", max_sum)
    print("Maximum Index :- ", max_row)
    max_sum=float('-inf')
    max_idx=-1
    # Brute Force
    for i in range(len(matrix)):
        row_sum=sum(matrix[i])
        print(row_sum)
        if row_sum>max_sum:
            max_sum=row_sum
            max_idx=i
    print("Maximum Sum :- ", max_sum)
    print("Maximum Index :- ", max_idx)


matrix=[[2,3,5],[5,6,7],[566,1,1]]
maximum(matrix)
# Set Matrix Zero
# Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

def zero(matrix,n,m):
    r=[0]*n
    c=[0]*m
    for i in range(n):
        for  j in range(m):
            if matrix[i][j]==0:
                r[i]=1
                c[j]=1
    for i in range(n):
        for j in range(m):
            if r[i] or c[i]:
                matrix[i][j]=0
    return matrix
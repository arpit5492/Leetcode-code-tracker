def SumDiag(matrix):
    add = 0
    for i in range(len(matrix)):
        # for j in range(len(matrix[0])):
        #     if i == j:
        #         add+=matrix[i][j]
        add+=matrix[i][i]
    return add

print(SumDiag([[1,2,3],
               [4,5,6],
               [7,8,9]]))
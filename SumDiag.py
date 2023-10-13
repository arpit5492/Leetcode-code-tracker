def SumDiag(matrix):
    t_sum = 0
    # for i in range(len(matrix)):
    #     # for j in range(len(matrix[0])):
    #     #     if i == j:
    #     #         add+=matrix[i][j]
    #     add+=matrix[i][i]
    # return add
    for i in range(len(matrix)):
            # for adding primary diagonal elements
        t_sum += matrix[i][i]
            # for adding secondary diagonal elements
        t_sum += matrix[len(matrix)-1-i][i]

    if len(matrix) % 2 != 0: t_sum -= matrix[len(matrix)//2][len(matrix)//2]
    return t_sum

# print(SumDiag([[1,2,3,4,5],
#                [4,5,6,7,8],
#                [7,8,9,10,11,12],
#                [1,2,3,4,5],
#                [1,2,3,4,5]]))

print(SumDiag([[1,2,3],
               [4,5,6],
               [7,8,9]]))
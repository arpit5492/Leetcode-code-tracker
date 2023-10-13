new_array = [[1,2,3],
             [4,5,6],
             [7,8,9]]
print(new_array)

def Rotmat(array):
    for i in range(len(array)):
        for j in range(i,len(array)):
            array[i][j],array[j][i] = array[j][i],array[i][j]
    for row in array:
        row.reverse()
    return array
print(Rotmat(new_array))


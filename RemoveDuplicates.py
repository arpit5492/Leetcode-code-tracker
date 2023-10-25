def RemoveDup(arr):
    # start pointer
    i = 0
    # end pointer
    j = i+1
    while(i<=j and j<len(arr)):        # 0 1 2 3 4 5 6 7 8 9
        if(arr[i] == arr[j]):          # 0 1 2 3 4
                                       #         i j
            j+=1
        else:
            arr[i+1]=arr[j]
            i+=1
    return i+1
        
# print(RemoveDup([0,0,1,1,1,2,2,3,3,4]))
print(RemoveDup([1,2,3]))

# 0 1 2 -> index
# 1 2 3 -> array
#     i j
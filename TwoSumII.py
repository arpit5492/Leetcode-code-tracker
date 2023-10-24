def twoSum(arr, target):
    # start pointer
    i = 0
    #end pointer
    j = len(arr)-1
    while i<j:
        s = arr[i] + arr[j]
        if(s == target):
            return [i+1,j+1]
        elif(s<target):
            i+=1
        else:
            j-=1
# print(twoSum([2,7,11,15],9)) 
print(twoSum([-1,0],-1))
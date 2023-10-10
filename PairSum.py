def PairSum(arr, target):
    lst = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                lst.append(str(arr[i])+ '+' +str(arr[j]))
            else: 
                continue
    return lst
print(PairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))
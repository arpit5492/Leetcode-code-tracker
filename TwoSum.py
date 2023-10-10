def TwoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                print([i,j])
            else:
                continue
(TwoSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))
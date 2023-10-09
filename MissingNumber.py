def missingNumber(arr, n):
    # add = 0
    # for i in range(n+1):
    #     add+=i
    # return (add - sum(arr))
    return (n*(n+1))//2 - sum(arr)
print(missingNumber([1,2,3,4,6],6))
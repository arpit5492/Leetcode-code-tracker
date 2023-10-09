def MaxProd(arr):
    arr.sort(reverse=True)
    return (arr[0]-1)*(arr[1]-1)
print(MaxProd([3,7]))
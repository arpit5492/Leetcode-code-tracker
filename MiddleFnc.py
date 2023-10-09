def MiddleFnc(array):
    a = len(array)//2
    if len(array) % 2 == 0:
        return [array[a-1],array[a]]
    else:
        return [array[a]]
print(MiddleFnc([1,2,3,4]))
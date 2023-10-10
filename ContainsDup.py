def ContainsDup(arr):
    found = set()
    for item in arr:
        if item in found:
            return True
        found.add(item)
    return False
print(ContainsDup([1,2,3]))
def RemoveDup(arr):
    new_list = []
    FoundItems = set()
    for item in arr:
        if item not in FoundItems:
            new_list.append(item)
            FoundItems.add(item)
    return (new_list)
print(RemoveDup([0,0,1,1,1,2,2,3,3,4]))
def lstodds(lst):
    oddlst = []    
    for num in lst:
        if not num % 2 ==0:
            oddlst.append(num)
    return oddlst

print(lstodds([1, 2, 3, 4, 5, 6, 7, 8]))





def lstevens(lst):
    evenlst = []
    for num in lst:
        if num % 2 ==0:
            evenlst.append(num)
    return evenlst

print(lstevens([1, 2, 3, 4, 5, 6, 7, 8]))
     


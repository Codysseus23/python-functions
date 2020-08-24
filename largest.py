def largest( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max

print(largest([1, 2, 3, 8, 19, 7]))   
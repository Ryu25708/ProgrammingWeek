def count_2Dn(m, x):
    count = 0
    i = 0   

    while i < len(m): 
        j = 0 
        while j < len(m[i]): 
            if m[i][j] == x:
                count = count + 1
            j = j + 1
        i = i + 1
    return count
m = [
    [1, 2, 3],
    [2, 4, 2],
    [5, 2, 6]
]

print(count_2Dn(m, 2))

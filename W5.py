a = [5, 9, 2]

max = a[0]
i = 1  # Yes, the index can start at 1

while i < len(a):
    if max < a[i]:
        max = a[i]
    i = i + 1

print(max)

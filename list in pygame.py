a = [3, 4, 2, 6, 5, 3, 4, 7, 8, 8, 3, 5, 3, 4, 2, 5, 4, 6, 2, 3]
i=0
while i < len(a):
    if a[i] == 5:
        a[i] = a[i] - 1
    i=i+1
print(a)
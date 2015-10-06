def insert(L, i):
    value = L[i]

    j = i
    while j != 0 and L[j - 1] > value:
        L[j] = L[j - 1]
        j = j - 1

    L[j] = value

L = [2, 5, 6, 7, 8, 0, 4]
print(L)
print("x = ",L[5])
insert(L,5)
print(L)

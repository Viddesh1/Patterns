# A                 a
# A B             a b
# A   C         a   c
# A     D     a     d
# 0       4 9       5
# 0     3     9     6
# 0   2         9   7
# 0 1             9 8
# 0                 9

n = 5

for i in range(n-1):

    p = 65
    for j in range(i+1):
        if j == 0 or i == j:
            print(chr(p), end=" ")
        else:
            print(" ",end=" ")
        p = p + 1

    for j in range(i, n-1):
        print(" ", end = " ")

    for j in range(i, n-1):
        print(" ", end=" ")
        
    p2 = 97
    for j in range(i+1):
        if j == 0 or j == i:
            print(chr(p2), end=" ")
        else:
            print(" ", end=" ")

        p2 = p2 + 1
        
    print()


for i in range(n):

    p3 = 48
    for j in range(i, n):
        if j == i or j == n-1:
            print(chr(p3), end=" ")
        else:
            print(" ", end = " ")

        p3 = p3 + 1

    for j in range(i):
        print(" ", end= " ")

    for j in range(i):
        print(" ", end=" ")

    p4 = 57
    for j in range(i, n):
        if i == j or j == n-1:
            print(chr(p4), end=" ")
        else:
            print(" ", end = " ")
        # print("&", end=" ")
        # print((i, j), end=" ")
        p4 = p4 - 1

    print()
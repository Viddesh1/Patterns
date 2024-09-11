#           a
#         b   b
#       c       c
#     d           d
#   e               e
#     f           f
#       g       g
#         h   h
#           i

n = 5
p = 97

for i in range(n-1):
    for j in range(i, n):
        print(" ", end = " ")

    for j in range(i):
        if j == 0:
            print(chr(p), end=" ")
        else:
            print(" ", end=" ")

    for j in range(i+1):
        if i == j:
            print(chr(p), end=" ")
        else:
            print(" ", end= " ")

    p = p + 1
    print()


for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")

    for j in range(i, n-1):
        if i == j:
            print(chr(p), end=" ")
        else:
            print(" ", end=" ")

    for j in range(i, n):
        if j == n-1:
            print(chr(p), end=" ")
        else:
            print(" ", end=" ")

    p = p + 1
    print()
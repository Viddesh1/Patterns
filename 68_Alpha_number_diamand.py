#           0
#         1 1 1
#       2 2 2 2 2
#     3 3 3 3 3 3 3
#   4 4 4 4 4 4 4 4 4
#     5 5 5 5 5 5 5
#       6 6 6 6 6
#         7 7 7
#           8


n = 5
p = 48

for i in range(n-1):
    for j in range(i, n):
        print(" ", end = " ")

    for j in range(i+1):
        print(chr(p), end=" ")

    for j in range(i):
        print(chr(p), end= " ")

    p = p + 1
    print()


for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")

    for j in range(i, n):
        print(chr(p), end=" ")

    for j in range(i, n-1):
        print(chr(p), end=" ")

    p = p + 1
    print()
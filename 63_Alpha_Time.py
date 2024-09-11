#   z z z z z Z Z Z Z
#     y y y y Y Y Y
#       x x x X X
#         w w W
#           v
#           9
#         8 8 1
#       7 7 7 2 2
#     6 6 6 6 3 3 3
#   5 5 5 5 5 4 4 4 4

n = 5
p = 122
p2 = 90
p3 = 57
p4 = 48

for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")

    for j in range(i, n):
        print(chr(p), end=" ")

    p = p - 1

    for j in range(i, n-1):
        print(chr(p2), end=" ")

    p2 = p2 - 1

    print()

for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")

    for j in range(i + 1):
        print(chr(p3), end=" ")
    
    p3 = p3 - 1

    for j in range(i):
        print(chr(p4), end = " ")

    p4 = p4 + 1

    print()

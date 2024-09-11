#   z z z z z Z Z Z Z
#     y y y y Y Y Y
#       x x x X X
#         w w W
#           v

n = 5
p = 122
p2 = 90

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

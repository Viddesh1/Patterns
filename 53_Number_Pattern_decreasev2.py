#   5 4 3 2 1
#     4 3 2 1
#       3 2 1
#         2 1
#           1

n = 5
k = 5

for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")

    p = k
    for j in range(i, n):
        print(p, end=" ")
        p = p - 1

    k = k - 1
    print()
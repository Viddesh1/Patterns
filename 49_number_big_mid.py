#      0
#     111
#    22222
#   3333333
#  444444444
#   3333333
#    22222
#     111
#      0

n = 5
p = 0

for i in range(n-1):
    for j in range(i, n):
        print(" ", end="")

    for j in range(i):
        print(p, end="")

    for j in range(i+1):
        print(p, end="")

    p = p + 1

    print()

for i in range(n):
    for j in range(i+1):
        print(" ", end="")
    
    for j in range(i, n-1):
        print(p, end="")

    for j in range(i, n):
        print(p, end="")

    p = p - 1

    print()
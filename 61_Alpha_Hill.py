#           a
#         b b b
#       c c c c c
#     d d d d d d d
#   e e e e e e e e e

n = 5
p = 97

for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")

    for j in range(i):
        print(chr(p), end=" ")

    for j in range(i+1):
        print(chr(p), end=" ")

    p = p + 1
    print()
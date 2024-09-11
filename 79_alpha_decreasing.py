#   E D C B A
#     D C B A
#       C B A
#         B A
#           A

n = 5
k = 69

for i in range(n):
    
    for j in range(i+1):
        print(" ", end=" ")

    p = k
    for j in range(i, n):
        print(chr(p), end=" ")
        p = p - 1
    
    k = k - 1

    print()
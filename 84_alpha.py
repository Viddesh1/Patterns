#   R E D O C
#     E D O C
#       D O C
#         O C
#           C


n = 5
s = "CODER"
n = len(s)
k = n-1

for i in range(n):
    
    for j in range(i+1):
        print(" ", end=" ")

    p = k
    for j in range(i, n):
        print(s[p], end=" ")
        p = p - 1
    
    k = k - 1

    print()
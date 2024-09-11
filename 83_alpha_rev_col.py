# R
# R E
# R E D
# R E D O
# R E D O C

n = 5
s = "CODER"
n = len(s)


for i in range(n):
    p = n-1
    for j in range(i+1):
        print(s[p], end=" ")
        p = p - 1
    print()
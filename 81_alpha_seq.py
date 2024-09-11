# C
# C O
# C O D
# C O D E
# C O D E R

n = 5
s = "CODER"
n = len(s)


for i in range(n):
    p = 0
    for j in range(i+1):
        print(s[p], end=" ")
        p = p + 1
    print()

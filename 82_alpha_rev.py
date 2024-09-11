# R
# E E
# D D D
# O O O O
# C C C C C

n = 5
s = "CODER"
n = len(s)
p = n - 1

for i in range(n):
    for j in range(i+1):
        print(s[p], end=" ")

    p = p - 1
    print()
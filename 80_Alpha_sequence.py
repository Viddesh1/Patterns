# C
# O O
# D D D
# E E E E
# R R R R R

n = 5
s = "CODER"
n = len(s)
p = 0

for i in range(n):
    for j in range(i+1):
        print(s[p], end=" ")

    p = p + 1
    print()

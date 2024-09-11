# A A A A A
# B B B B
# C C C
# D D
# E

n = 5
p = 65

for i in range(n):
    for j in range(i, n):
        print(chr(p), end=" ")

    p = p + 1
    print()
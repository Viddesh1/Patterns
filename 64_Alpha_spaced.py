# A A A A A
# F F F F
# K K K
# P P
# U

n = 5
p = 65

for i in range(n):
    for j in range(i, n):
        print(chr(p), end=" ")

    p = p + 5
    print()
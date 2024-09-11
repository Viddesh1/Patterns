# A          a
# BB        bb
# CCC      ccc
# DDDD    dddd
# 00000  99999
# 1111    8888
# 222      777
# 33        66
# 4          5

n = 5
p = 65
p2 = 97
p3 = 48
p4 = 57

for i in range(n-1):
    for j in range(i+1):
        print(chr(p), end="")

    p = p+1

    for j in range(i, n):
        print(" ", end="")

    for j in range(i, n):
        print(" ", end="")

    for j in range(i+1):
        print(chr(p2), end="")

    p2 = p2 + 1

    print()

for i in range(n):
    for j in range(i, n):
        print(chr(p3), end="")

    p3 = p3 + 1

    for j in range(i+1):
        print(" ", end="")

    for j in range(i+1):
        print(" ", end="")

    for j in range(i, n):
        print(chr(p4), end="")

    p4 = p4 - 1
    print()
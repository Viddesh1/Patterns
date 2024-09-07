# 0 1
# 0 1 0 1
# 0 1 0 1 0 1
# 0 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0 1 0 1

n = 5
p = 0

for i in range(0, n):
    for j in range(i + 1):
        if p == 0:
            print(p, end=" ")
            p = p + 1
        if p == 1:
            print(p, end = " ")
            p = p - 1

    print()
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4

n = 5

for i in range(n):
    p = 0
    for j in range(i + 1):
        print(p, end=" ")
        p = p + 1

    print()
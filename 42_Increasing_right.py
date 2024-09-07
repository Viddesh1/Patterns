# 0
# 1 1
# 2 2 2
# 3 3 3 3
# 4 4 4 4 4

n = 5
p = 0

for i in range(0, n):
    for j in range(i + 1):
        print(p, end=" ")

    p = p + 1

    print()
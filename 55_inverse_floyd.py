# 15
# 14 13
# 12 11 10
# 9 8 7 6
# 5 4 3 2 1

n = 5
p = 15

for i in range(n):
    for j in range(i+1):
        print(p, end=" ")
        p = p - 1

    print()
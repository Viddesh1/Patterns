# 1
# 1 2
# 1 2 1
# 1 2 1 2
# 1 2 1 2 1

n = 5

for i in range(n):
    p = 0
    for j in range(i + 1):
        if p % 2 == 0:
            print("1", end=" ")
        else:
            print("2", end=" ")
        p = p + 1
    
    print()
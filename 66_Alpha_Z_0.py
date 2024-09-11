# Z
# 0 0
# Z Z Z
# 0 0 0 0
# Z Z Z Z Z

n = 5

for i in range(n):
    for j in range(i+1):
        if i % 2 == 0:
            print('Z', end=" ")
        else:
            print('0', end=" ")

    print()
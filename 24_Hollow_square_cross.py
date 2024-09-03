# * * * * * * * * * *
# * *             * *
# *   *         *   *
# *     *     *     *
# *       * *       *
# *       * *       *
# *     *     *     *
# *   *         *   *
# * *             * *
# * * * * * * * * * *

n = 5

for i in range(n):
    for j in range(i+1):
        if j == 0 or i == j:
            print("*", end=" ")
        else:
            print(" ",end=" ")
        # print((i, j), end = " ")

    for j in range(i, n-1):
        if i == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    for j in range(i, n-1):
        if i == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    for j in range(i+1):
        if j == 0 or i == j:
            print("*", end=" ")
        else:
            print(" ", end = " ")

    print()


for i in range(n):
    for j in range(i, n):
        if i == j or j == n-1:
            print("*", end = " ")
        else:
            print(" ", end= " ")

    for j in range(i):
        if i == n-1:
            print("*", end= " ")
        else:
            print(" ", end= " ")

    for j in range(i):
        if i == n-1:
            print("*", end= " ")
        else:
            print(" ", end= " ")

    for j in range(i, n):
        if i == j or j == n-1:
            print("*", end= " ")
        else:
            print(" ", end= " ")
        # print((i, j), end=" ")

    print()
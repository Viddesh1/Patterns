#   * * * * * * * * *
#     *           *
#       *       *
#         *   *
#           *

n = 5

for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")

    for j in range(i, n-1):
        if i == 0 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    for j in range(i, n):
        if i == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
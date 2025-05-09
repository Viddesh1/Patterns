r"""Pattern for capital K"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 5):
        print((i, j, "*"), end="")
    print(end="\n")


# TODO: Capital K
# for i in range(0, 10):
#     for j in range(0, 5):
#         if (j == 0) or (i + j == 4) : # or (i + j == )
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print(end="\n")

i = 0
j = 4
for row in range(7):
    for col in range(5):
        if col == 0 or (row == col + 2 and col > 1):
            print("*", end="")
        elif ((row == i and col == j) and col > 0):
            print("*", end="")
            i = i + 1
            j = j - 1
        else:
            print(end=" ")
    print()


# *   *
# *  * 
# * *  
# **   
# * *  
# *  * 
# *   *
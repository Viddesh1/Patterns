r"""Pattern for capital D"""

# For reasoning
# for i in range(10):
#     for j in range(10):
#         print((i, j, "*"), end="")
#     print(end="\n")


# Implementation
for i in range(10):
    for j in range(10):
        if (j == 0) or (i == 0 and j < 9) or (j == 9 and i >= 1 and i <= 8) or (i == 9 and j <= 8):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# *********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *********
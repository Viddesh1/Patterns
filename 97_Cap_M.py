r"""Pattern for capital M"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")


# Capital M
for i in range(0, 10):
    for j in range(0, 10):
        if (j == 0) or (j == 9) or ((i == j) and (i <= 4 and j <= 4)) or ((i + j == 9) and (i <= 4)):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")

# *        *
# **      **
# * *    * *
# *  *  *  *
# *   **   *
# *        *
# *        *
# *        *
# *        *
# *        *

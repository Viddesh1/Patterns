r"""Pattern for capital N"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")


# Capital N
for i in range(0, 10):
    for j in range(0, 10):
        if (j == 0) or (j == 9) or ((i == j)):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")

# *        *
# **       *
# * *      *
# *  *     *
# *   *    *
# *    *   *
# *     *  *
# *      * *
# *       **
# *        *
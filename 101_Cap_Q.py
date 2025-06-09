r"""Pattern for capital Q"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")

print("\n")

# Capital Q (Square)
for i in range(0, 10):
    for j in range(0, 10):
        if (i <= 7 and j == 0) or (i == 0) or (j == 9 and i <= 7) or (i == 7) or ((i == j) and (i >= 5 and j >= 5)):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")


# **********
# *        *
# *        *
# *        *
# *        *
# *    *   *
# *     *  *
# **********
#         *
#          *
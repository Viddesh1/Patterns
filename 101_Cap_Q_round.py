r"""Pattern for capital Q"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")

print("\n")

# Capital Q (Round)
for i in range(0, 10):
    for j in range(0, 10):
        if ((i >= 1 and i <= 6) and j == 0) or (i == 0 and (j >= 1 and j <= 8)) or (j == 9 and (i >= 1 and i <= 6)) or (i == 7 and (j >= 1 and j <= 8)) or ((i == j) and (i >= 5 and j >= 5)):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")


#  ********
# *        *
# *        *
# *        *
# *        *
# *    *   *
# *     *  *
#  ********
#         *
#          *
r"""Pattern for capital L"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")


# Capital L
for i in range(0, 10):
    for j in range(0, 10):
        if (j == 0) or (i == 9):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# *         
# *         
# *         
# *         
# *         
# *         
# *         
# *         
# *         
# **********
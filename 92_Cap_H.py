r"""Pattern for capital G"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")


for i in range(0, 10):
    for j in range(0, 10):
        if (j == 0) or (i == 4) or (j == 9):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")

# *        *
# *        *
# *        *
# *        *
# **********
# *        *
# *        *
# *        *
# *        *
# *        *
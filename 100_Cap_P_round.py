r"""Pattern for capital O"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")


print("\n")

# Capital P (Square)
for i in range(0, 10):
    for j in range(0, 10):
        if (i == 0 and j <= 8) or ((i <= 4 and i >= 1) and j == 9) or (i == 5 and j <= 8) or (j == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")


# *********
# *        *
# *        *
# *        *
# *        *
# *********
# *
# *
# *
# *
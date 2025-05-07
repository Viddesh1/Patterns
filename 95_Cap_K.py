r"""Pattern for capital K"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 5):
        print((i, j, "*"), end="")
    print(end="\n")


# TODO: Capital K
for i in range(0, 10):
    for j in range(0, 5):
        if (j == 0) or (i + j == 4) or (i + j == ):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")
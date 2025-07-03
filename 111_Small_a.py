r"""Pattern for small letter a"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")

print("\n")

# Small a (Square)
for i in range(0, 10):
    for j in range(0, 10):
        if (i == 0) or (j == 9) or (i == 9) or (i == 5) or (j == 0 and (i >= 5 and i <= 9)):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")



r"""Pattern for small letter b"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")

print("\n")

# Small a (Square)
for i in range(0, 10):
    for j in range(0, 10):
        if (j == 0) or (i == 4) or (j == 9 and (i >= 4 and i <= 8)) or (i == 8):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")


# *         
# *         
# *         
# *         
# **********
# *        *
# *        *
# *        *
# **********
# *   
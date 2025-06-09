r"""Pattern for small y"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")

print("\n")

# Small y (Square)
for i in range(0, 10):
    for j in range(0, 10):
        if (j == 0 and (i >= 0 and i <= 3)) or (i == 3) or (j == 9 and (i >= 0 and i <= 3)) or (j == 9) or (i == 9):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")



# *        *
# *        *
# *        *
# **********
#          *
#          *
#          *
#          *
#          *
# **********
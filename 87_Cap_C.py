r"""Pattern for capital C (Round and Square)"""

# For reasoning
# for i in range(10):
#     for j in range(10):
#         print((i, j, "*"), end="")
#     print(end="\n")


# Implementation
for i in range(10):
    for j in range(10):
        if (j == 0 and i >= 1 and i <= 8) or (i == 0 and j >= 1) or (i == 9 and j >= 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()


#  *********
# *
# *
# *
# *
# *
# *
# *
# *
#  *********

print("\n ################# \n")

for i in range(10):
    for j in range(10):
        if (j == 0) or (i == 0) or (i == 9):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# **********
# *
# *
# *
# *
# *
# *
# *
# *
# **********
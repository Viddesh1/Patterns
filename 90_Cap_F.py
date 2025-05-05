r"""Pattern for capital F"""

# For reasoning
# for i in range(10):
#     for j in range(10):
#         print((i, j, "*"), end="")
#     print(end="\n")


# Implementation
for i in range(0, 10):
    for j in range(0, 10):
        if (i == 0) or (i == 4) or (j == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")


# **********
# *         
# *         
# *         
# **********
# *         
# *         
# *         
# *         
# * 
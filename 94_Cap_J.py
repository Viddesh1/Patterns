r"""Pattern for capital J"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")


# Square like J
for i in range(0, 10):
    for j in range(0, 10):
        if (i == 0) or (j == 4) or (i == 9 and j <= 4) or (j == 0 and i >= 5):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")

# **********
#     *     
#     *     
#     *     
#     *     
# *   *     
# *   *     
# *   *     
# *   *     
# *****   


# Round like capital J
for i in range(0, 10):
    for j in range(0, 10):
        if (i == 0) or (j == 4 and i <= 8) or (i == 9 and j >= 1 and j <= 3) or (j == 0 and i >= 5 and i <= 8):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")


# **********
#     *     
#     *     
#     *     
#     *     
# *   *     
# *   *     
# *   *     
# *   *     
#  ***  
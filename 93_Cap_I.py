r"""Pattern for capital I"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")


for i in range(0, 10):
    for j in range(0, 10):
        if (i == 0) or (j == 4) or (i == 9):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")

# **********
#     *     
#     *     
#     *     
#     *     
#     *     
#     *     
#     *     
#     *     
# **********
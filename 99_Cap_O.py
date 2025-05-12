r"""Pattern for capital O"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")


# Capital O
for i in range(0, 10):
    for j in range(0, 10):
        if (i == 0 and (j >= 1 and j <= 8)) or (j == 0 and (i >= 1 and i <= 8)) or (i == 9 and (j >= 1 and j <= 8)) or (j == 9 and (i >= 1 and i <= 8)):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")



#  ******** 
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
#  ******** 
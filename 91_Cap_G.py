r"""Pattern for capital G"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")

# G (Square)
for i in range(0, 10):
    for j in range(0, 10):
        if (i == 0) or (j == 0) or (i == 9) or (j == 9 and i >=4) or (i == 4 and j >= 4):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")

# **********
# *         
# *         
# *         
# *   ******
# *        *
# *        *
# *        *
# *        *
# **********

print("#"*50)

for i in range(0, 10):
    for j in range(0, 10):
        if (i == 0 and j >= 1) or (j == 0 and i >= 1 and i <= 8) or (i == 9 and j >= 1 and j <=8) or (j == 9 and i >=5 and i <= 8) or (i == 4 and j >= 4 and j <=8):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")


#  *********
# *         
# *         
# *         
# *   ***** 
# *        *
# *        *
# *        *
# *        *
#  ******** 
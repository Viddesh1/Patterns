r"""Pattern for capital R"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")

print("\n")

# Capital R (Square)
for i in range(0, 10):
    for j in range(0, 10):
        if (j == 0) or (i == 0) or (i <= 5 and j == 9) or (i == 5) or (i == j and (i >=5 and j >=5)):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")



# **********
# *        *
# *        *
# *        *
# *        *
# **********
# *     *   
# *      *  
# *       * 
# *        *
r"""Pattern for capital R"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")

print("\n")

# Capital R (Round)
for i in range(0, 10):
    for j in range(0, 10):
        if (j == 0 and i >= 1) or (i == 0 and (j >= 1 and j <= 8)) or ((i >= 1 and i <= 4) and j == 9) or (i == 5 and (j >= 1 and j <= 8)) or (i == j and (i >=5 and j >=5)):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")



#  ******** 
# *        *
# *        *
# *        *
# *        *
# ********* 
# *     *   
# *      *  
# *       * 
# *        *
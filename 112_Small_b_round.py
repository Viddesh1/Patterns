r"""Pattern for small letter b (round)"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")

print("\n")

# Small a (Square)
for i in range(0, 10):
    for j in range(0, 10):
        if (i == 0 and j == 0) or (j == 1 and (i >= 1 and i <= 8)) or (i == 4 and (j >= 1 and j <= 8)) or ((i >= 5 and i <= 7) and j == 9) or (i == 8 and (j >= 1 and j <= 8)) or (i == 9 and j == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")


# *         
#  *        
#  *        
#  *        
#  ******** 
#  *       *
#  *       *
#  *       *
#  ******** 
# *    
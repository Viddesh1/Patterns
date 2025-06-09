r"""Pattern for capital S"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")

print("\n")

# Capital S (Square)
for i in range(0, 10):
    for j in range(0, 10):
        if ((j >= 1 and j <= 8) and i == 0) or ((i >= 1 and i <= 4) and j == 0) or (i == 5 and (j >= 1 and j <= 8)) or ((i >=6 and i <= 8) and j == 9) or (i == 9 and j <= 8):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")



#  ******** 
# *         
# *         
# *         
# *         
#  ******** 
#          *
#          *
#          *
# ********* 
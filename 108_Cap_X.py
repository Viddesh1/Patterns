r"""Pattern for capital X"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")

print("\n")

# Capital X (Square)
for i in range(0, 10):
    for j in range(0, 10):
        if (i == j) or (i + j == 9):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")



# *        *
#  *      * 
#   *    *  
#    *  *   
#     **    
#     **    
#    *  *   
#   *    *  
#  *      * 
# *        *
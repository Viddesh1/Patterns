r"""Pattern for capital Y"""

# For reasoning
for i in range(0, 11):
    for j in range(0, 11):
        print((i, j, "*"), end="")
    print(end="\n")

print("\n")

# Capital Y (Square)
for i in range(0, 10):
    for j in range(0, 10):
        if (i == j and (i <= 5 and j <= 5 and not (i == 0 and j == 0))) or (i + j == 10 and i <= 4 and j <= 10) or (j == 5 and i >= 6):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")


#  *       *
#   *     * 
#    *   *  
#     * *   
#      *    
#      *    
#      *    
#      *    
#      * 
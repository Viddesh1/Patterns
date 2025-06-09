r"""Pattern for capital W"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")

print("\n")

# Capital W (Square)
for i in range(0, 10):
    for j in range(0, 10):
        if i == j:
            print("*", end="")
        else:
            print(" ", end="")
    
    for j in range(0, 10):
        if (i + j) == 9:
            print("*", end="")
        else:
            print(" ", end="")

    for j in range(0, 10):
        if i == j:
            print("*", end="")
        else:
            print(" ", end="")
    
    for j in range(0, 10):
        if (i + j) == 9:
            print("*", end="")
        else:
            print(" ", end="")
    
    print(end="\n")


# *                  **                  *
#  *                *  *                * 
#   *              *    *              *  
#    *            *      *            *   
#     *          *        *          *    
#      *        *          *        *     
#       *      *            *      *      
#        *    *              *    *       
#         *  *                *  *        
#          **                  **   
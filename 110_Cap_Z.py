r"""Pattern for capital Z"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")

print("\n")

# Capital Z (Square)
for i in range(0, 10):
    for j in range(0, 10):
        if (i == 0) or (i + j == 9) or (i == 9):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")


# **********
#         * 
#        *  
#       *   
#      *    
#     *     
#    *      
#   *       
#  *        
# **********


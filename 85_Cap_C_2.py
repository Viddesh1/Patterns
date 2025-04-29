r"Pattern of capital C"


for i in range(7):
    for j in range(5):
        if (i == 0 and j > 0) or (j == 0 and i > 0 and i < 6) or (i == 6 and j > 0):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")

#  ****
# *    
# *    
# *    
# *    
# *    
#  ****
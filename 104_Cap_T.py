r"""Pattern for capital T"""

# For reasoning
for i in range(0, 10):
    for j in range(0, 10):
        print((i, j, "*"), end="")
    print(end="\n")

print("\n")

# Capital T (Square)
for i in range(0, 5):
    for j in range(0, 5):
        if (i == 0) or (j == 2):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")



# *****
#   *  
#   *  
#   *  
#   * 
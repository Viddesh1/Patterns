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
        if (i == 0) or ((i >= 0 and i <= 5) and j == 0) or (i == 5) or (i >=5 and j == 9) or (i == 9):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")



# **********
# *         
# *         
# *         
# *         
# **********
#          *
#          *
#          *
# **********
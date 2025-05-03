r"""Pattern of capital B"""

# Print one condition in round bracket at a time for debugging or learning again.



for i in range(0, 7):
    for j in range(0, 5):
        if (j==0 or (i == 6 and j < 4)) or (i==0 and j<4) or (j==4 and (i > 0 and i < 3)) or (i == 3 and j < 4) or (j == 4 and (i > 3 and i < 6)):
            print("*", end="")
        else:
            print(" ", end="")
    print()



# ****
# *   *
# *   *
# ****
# *   *
# *   *
# ****
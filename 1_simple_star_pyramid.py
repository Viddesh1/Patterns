# *
# **
# ***
# ****
# *****

# breakpoint()
for i in range(5):
    for j in range(i+1):
        print('*', end="")

    print()

# ---------------------------------------
# How to debug?
# Create a breakpoint where you want to be.
# python -m pdb my_script_name.py
# ---------------------------------------
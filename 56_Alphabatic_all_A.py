#   ASCI Code of characters
#   +_________________________________________+
#   | ASCII Characters    |   ASCII Codes     |
#   |_____________________|___________________|
#   |   A to Z            |   [65 - 90]       | Difference 25
#   |   a to z            |   [97 - 122]      | Difference 25
#   |   0 to 9            |   [48 - 57]       | Difference 9
#   +-----------------------------------------+

# A
# A A
# A A A
# A A A A
# A A A A A

n = 5

for i in range(n):
    for j in range(i + 1):
        print(chr(65), end=" ")
    
    print()
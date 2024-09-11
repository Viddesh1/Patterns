# A E D C B A
# A B E D C B
# A B C E D C
# A B C D E D
# A B C D E E

n = 5

for i in range(n):
    p = 65
    for j in range(i+1):
        print(chr(p), end=" ")
        p = p + 1


    p2 = 69
    for j in range(i, n):
        print(chr(p2), end=" ")
        p2 = p2 - 1

    print()
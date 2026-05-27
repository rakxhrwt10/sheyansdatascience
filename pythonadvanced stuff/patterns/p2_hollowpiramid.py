# n = 6

# for i in range(n):

#     # spaces
#     for s in range(n - i):
#         print(" ", end='')

#     # stars
#     for j in range(2 * i + 1):
#         if i==2 or i==4 or i==6:

#             print("*",end='')

#     print()



n = 6

for i in range(n):

    # spaces
    for s in range(n - i - 1):
        print(" ", end='')

    # stars and hollow part
    for j in range(2 * i + 1):

        # first star
        # last star
        # full last row
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end='')

        else:
            print(" ", end='')

    print()
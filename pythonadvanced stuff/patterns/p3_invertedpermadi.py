# # n = 6

# # for i in range(n):

# #     # spaces
# #     for s in range(n - i):
# #         print(" ", end='')

# #     # stars
# #     for j in range(2 * i + 1):
# #         if i==2 or i==4 or i==6:

# #             print("*",end='')

# #     print()



# n = 6

# for i in range(n):

#     for s in range(i):
#         print(" ",end='')

#     for c in range(n-i,1,-1):

#         print(" * ",end='')
#     print()




n = 6

for i in range(n):

    for s in range(i):
        print(" ", end='')

    for j in range(2*(n-i)-1):
        print("*", end='')

    print()    
def toBinary(n):
    #Your code here
    binary = ""
    while n > 0:
        binary += str(n%2)
        n = int(n/2)
    return binary[::-1] 
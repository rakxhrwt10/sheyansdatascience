# def Replace(n: int):
#     string = str(n)
#     result = ""

#     for ch in string:
#         if ch == '0':
#             result += '5'
#         else:
#             result += ch

#     return int(result)

# print(Replace(1200))




# def Replace(n: int):
#     if n == 0:
#         return 5

#     result = 0
#     place = 1

#     while n > 0:
#         digit = n % 10

#         if digit == 0:
#             digit = 5

#         result = digit * place + result
#         place *= 10
#         n //= 10

#     return result
# print("hello".replace())
def SecondMax(lst:list):



    maxx=lst[0]
    secodMax=lst[0]

    for s in range(1,len(lst)):
      if maxx<lst[s]:

        maxx=lst[s]

    for l in range(0,len(lst)):
       
       if lst[l]!= maxx and secodMax<lst[l]:
          
          secodMax=lst[l]

    return secodMax


          
          

    

    

print(SecondMax([500,2,3,1000,4,5]))
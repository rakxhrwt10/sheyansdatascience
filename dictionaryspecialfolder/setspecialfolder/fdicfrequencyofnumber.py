


l=[1,1,1,2,2,2,2,2,3,4,4,4,5,6]

def FreqQuecy(lst:list):
    b={}


    for i in l:


        if i in b:
            b[i]+=1

        else:

            b[i]=1

    return b,b.keys()

        

# l=[1,1,1,2,2,2,2,2,3,4,4,4,5,6]

result=FreqQuecy(l)
print(result)








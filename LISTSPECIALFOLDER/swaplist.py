def Swap(lst:list):

    i=0
    j=lst[i+1]

    for s in range(0,len(lst)-1,-2):

        lst[s],lst[s+1]=lst[s+1],lst[s]

       


    return lst

print(Swap([1,2,3,4]))
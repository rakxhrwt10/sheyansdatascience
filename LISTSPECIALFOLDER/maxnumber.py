def MaxNumber(lst:list):

    Max_num=float("-inf")
    length_list=len(lst)

    for num in range(0,length_list):

        if lst[num]>Max_num:
            Max_num=lst[num]
    return Max_num


li_Max_num=MaxNumber([100000,10000010000010,10,20,300,10,300,])

print(li_Max_num)





    
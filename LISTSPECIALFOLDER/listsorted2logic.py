def  Sorted_list(lst:list):

    for i in range(len(lst)-1):

        if lst[i]<lst[i+1]:

            continue
        else:
            print("array is not sorted")
            break

Sorted_list([1,2,3,4,5])

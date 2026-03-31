def sumOfUnique(nums: list) -> int:



        d={}


        for n in nums:


            if  n in d:



                d[n]+=1

            else:

                d[n]=1
        summ=0

        for j in d:
            if d[j]==1:

                summ+=j

        return summ

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

def SecondMax(lst: list):

    maxx = lst[0]
    secodMax = float('-inf')   # important fix

    # find max
    for s in range(1, len(lst)):
        if maxx < lst[s]:
            maxx = lst[s]

    # find second max
    for l in range(len(lst)):
        if lst[l] != maxx and secodMax < lst[l]:
            secodMax = lst[l]

    return secodMax
          
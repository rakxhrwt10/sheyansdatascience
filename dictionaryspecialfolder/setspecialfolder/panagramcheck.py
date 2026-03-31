def PanagramCheck(setence:str):


    d={}


    for s in setence:

        if s in d.keys():

            d[s]+=1

        else:

            d[s]=1

    if len(d)==26:
        return True
    
    else:

        return False


print(PanagramCheck("hellojixcootu"))





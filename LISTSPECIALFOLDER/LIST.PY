li=[]

for i in range(1,10):

    if i%2==0 :
        li.append(i)

print(li)


st=["jello","jiyan","kewish","kaipur"]
clean_list=[]

for s in  st:

    clean_list.append(s[0:].replace("j","h"))

print(clean_list)
    
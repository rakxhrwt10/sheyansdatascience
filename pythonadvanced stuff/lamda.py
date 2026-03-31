#without lambda


def sum(a,b):

    return a+b


print(sum(9,9.0))


#with labmda


s=lambda x,y: x+y

print(s(9,9))


#MAP 

#purpose➡️ appy function to every item of an iterable an return a new iterable

#syntax map(function,iterable)

#without map print squar every item


# l=[1,2,3,4,5]

# b=[]

# for i in l:


#     b.append(i**2)

# print(l)
# print(b)

#with map and lamda

a=[1,2,3,4,5]


b=list(map(lambda x:x**2,a))

print(b)
print(a)

#filter purpose➡️ filter an item based on condition

#syntax filter(function,iterable)


li=[x for x in range(1,20)]

evenfil=list(filter(lambda x:x%2==0,li))

oddfil=list(filter(lambda x:x%2!=0,li))

print(f'even num:{evenfil} \nodd num:{oddfil}')



#zip

#purpose➡️combine multiple iterables into pairs of elements
#syntax zip(itreble1,itreble,...)

name=['Alice','Bob','Charlie']
age=[25,30,35]
zipped=list(zip(name,age))
combined=dict(zip(name,age))
tupled=tuple(zip(name,age))
print(zipped)
print(combined)
print(tupled)





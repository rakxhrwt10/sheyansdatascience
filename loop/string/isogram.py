def isogram(st: str):
    st = st.lower()
    
    d = {}

    for ch in st:
        if ch in d:
            return False
        d[ch] = 1

    return True


print(isogram("lampm"))   # True
print(isogram("hello"))  # False


# def isogram(st):
#     st = st.lower()
#     return len(st) == len(set(st))

#brute force approach


# def isogram(st: str):#hello
#     st = st.lower()

#     for i in range(len(st)):#len(st)-->5
#         for j in range(i + 1, len(st)):#next element j-->e
#             if st[i] == st[j]:#st[0]-->h st[1]-->e
#                 return False

#     return True


# print(isogram("lamp"))   # True
# print(isogram("hello"))  # False
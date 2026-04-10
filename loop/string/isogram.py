def isogram(st: str):
    st = st.lower()
    
    d = {}

    for ch in st:
        if ch in d:
            return False
        d[ch] = 1

    return True


print(isogram("lamp"))   # True
print(isogram("hello"))  # False
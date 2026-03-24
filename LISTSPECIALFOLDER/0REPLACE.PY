def Replace(n: int):
    string = str(n)
    result = ""

    for ch in string:
        if ch == '0':
            result += '5'
        else:
            result += ch

    return int(result)

print(Replace(1200))
# print("hello".replace())
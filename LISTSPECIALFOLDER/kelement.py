def kelment(so, k):

    for s in range(len(so)):
        if so[s] == k:
            return s + 1   # 👈 yaha change

print(kelment([1,2,2,4,5,5,5,5], 2))


def kelment(so, k):
    return so.index(k) if k in so else -1
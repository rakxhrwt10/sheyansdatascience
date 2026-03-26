def is_sorted(lst: list):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
            





# def is_sorted(lst):
#     i = 0
#     j = 1

#     while j < len(lst):
#         if lst[i] > lst[j]:
#             return False
#         i += 1
#         j += 1

#     return True

print(is_sorted([12,13,14,15,16]))



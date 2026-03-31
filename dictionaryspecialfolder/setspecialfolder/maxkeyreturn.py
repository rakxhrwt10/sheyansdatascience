def key_with_max_value(d):

    if d==False :return None
    max_key = None
    max_value = float('-inf')

    for key, value in d.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key

def dic_depth(dic):
    if dic == {}:
        return 0
    res = 1
    for v in dic.values():
        if isinstance(v, dict) and dic_depth(v) + 1 > res:
            res = 1 + dic_depth(v)
    return res


print(dic_depth({'one': 1, '2': {'three': {'a': 1}, 'four': {'a': {'c': 1}}}}))

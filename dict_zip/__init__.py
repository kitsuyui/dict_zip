import functools


def dict_zip(*dictionaries):
    common_keys = functools.reduce(
        lambda x, y: x & y, (set(d.keys()) for d in dictionaries)
    )
    return_dic = {}
    for dic in dictionaries:
        for key, val in dic.items():
            if key in common_keys:
                return_dic.setdefault(key, []).append(val)

    return {key: tuple(val) for key, val in return_dic.items()}


def dict_zip_longest(*dictionaries, fillvalue=None):
    all_keys = __all_keys(d.keys() for d in dictionaries)
    return_dic = {key: tuple() for key in all_keys}

    for dic in dictionaries:
        for key in all_keys:
            return_dic[key] += (dic.get(key, fillvalue),)

    return return_dic


def __all_keys(iterables):
    keys = []
    for iterable in iterables:
        for key in iterable:
            if key in keys:
                continue
            keys.append(key)
    return keys

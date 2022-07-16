import functools


def dict_zip(*dictionaries):
    """Returns a new dictionary \
concatenated with the dictionaries specified in the argument.

    The key is a common key that each dictionary has.
    The value is a tuple of the values of the dictionaries.

    >>> dict_zip({'a': 1, 'b': 2}, {'a': 3, 'b': 4})
    {'a': (1, 3), 'b': (2, 4)}
    """
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
    """Returns a new dictionary \
concatenated with the dictionaries specified in the argument.

    The keys are the union set of the dictionaries.
    The value is a tuple of the values of the dictionaries.
    If the specified dictionary does not have the key, \
it is filled with fillvalue (default: None).

    >>> dict_zip_longest({'a': 1, 'b': 2, 'c': 4}, {'a': 3, 'b': 4})
    {'a': (1, 3), 'b': (2, 4), 'c': (4, None)}
    """
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

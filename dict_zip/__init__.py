import functools


def dict_zip(*dictionaries):
    common_keys = functools.reduce(lambda x, y: x | y,
                                   (set(d.keys()) for d in dictionaries),
                                   set())
    return {
        key: tuple(d[key] for d in dictionaries)
        for key in common_keys
        if all(key in d for d in dictionaries)
    }


def dict_zip_longest(*dictionaries, fillvalue=None):
    common_keys = functools.reduce(lambda x, y: x | y,
                                   (set(d.keys()) for d in dictionaries),
                                   set())
    return {
        key: tuple(d.get(key, fillvalue) for d in dictionaries)
        for key in common_keys
    }

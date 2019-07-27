import functools


def dict_zip(*dictionaries):
    common_keys = functools.reduce(lambda x, y: x | y,
                                   (set(d.keys()) for d in dictionaries),
                                   set())
    for key in common_keys:
        if any(key not in d for d in dictionaries):
            continue
        yield key, tuple(d[key] for d in dictionaries)


def dict_zip_longest(*dictionaries):
    common_keys = functools.reduce(lambda x, y: x | y,
                                   (set(d.keys()) for d in dictionaries),
                                   set())
    for key in common_keys:
        yield key, tuple(d.get(key, None) for d in dictionaries)

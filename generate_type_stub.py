NUMBER_OF_ITERATORS = 10

print("""\
from typing import (
    Any,
    Dict,
    Optional,
    overload,
    Tuple,
    TypeVar,
    Union,
)""")
print()
print()
print("""K = TypeVar('K')""")
print("""Fill = TypeVar('Fill')""")
for i in range(1, NUMBER_OF_ITERATORS):
    print(f"""_T{i} = TypeVar('_T{i}')""")
print()
print()
print("# type stubs for dict_zip")
for i in range(1, NUMBER_OF_ITERATORS):
    arguments = ', '.join(f'dict{j}: Dict[K, _T{j}]' for j in range(1, 1 + i))
    return_tuple_types = ', '.join(f'_T{j}' for j in range(1, 1 + i))
    returns = f'Dict[K, Tuple[{return_tuple_types}]]'
    print(f"""\
@overload
def dict_zip({arguments}) -> {returns}: ...""")
print()
print()
print("# type stubs for dict_zip_longest")
for i in range(1, NUMBER_OF_ITERATORS):
    arguments = ', '.join(f'dict{j}: Dict[K, _T{j}]' for j in range(1, 1 + i))
    return_tuple_types = ', '.join(f'Optional[_T{j}]'
                                   for j in range(1, 1 + i))
    returns = f'Dict[K, Tuple[{return_tuple_types}]]'
    print(f"""\
@overload
def dict_zip_longest({arguments}) -> {returns}: ...""")
    return_tuple_types = ', '.join(f'Union[_T{j}, Fill]'
                                   for j in range(1, 1 + i))
    returns = f'Dict[K, Tuple[{return_tuple_types}]]'
    print(f"""\
@overload
def dict_zip_longest({arguments},
                     *,
                     fillvalue: Fill = ...) -> {returns}: ...""")

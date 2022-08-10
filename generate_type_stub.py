NUMBER_OF_ITERATORS = 10

print("""\
from typing import (
    Any,
    Optional,
    overload,
    TypeVar,
    Union,
)""")
print()
print()
print("""_K = TypeVar('_K')""")
print("""_Fill = TypeVar('_Fill')""")
for i in range(1, NUMBER_OF_ITERATORS):
    print(f"""_T{i} = TypeVar('_T{i}')""")
print()
print()
print("# type stubs for dict_zip")
for i in range(1, NUMBER_OF_ITERATORS):
    arguments = ', '.join(f'dict{j}: dict[_K, _T{j}]' for j in range(1, 1 + i))
    return_tuple_types = ', '.join(f'_T{j}' for j in range(1, 1 + i))
    returns = f'dict[_K, tuple[{return_tuple_types}]]'
    print(f"""\
@overload
def dict_zip({arguments}) -> {returns}: ...""")
print()
print()
print("# type stubs for dict_zip_longest")
for i in range(1, NUMBER_OF_ITERATORS):
    arguments = ', '.join(f'dict{j}: dict[_K, _T{j}]' for j in range(1, 1 + i))
    return_tuple_types = ', '.join(f'Optional[_T{j}]'
                                   for j in range(1, 1 + i))
    returns = f'dict[_K, tuple[{return_tuple_types}]]'
    print(f"""\
@overload
def dict_zip_longest({arguments}) -> {returns}: ...""")
    return_tuple_types = ', '.join(f'Union[_T{j}, _Fill]'
                                   for j in range(1, 1 + i))
    returns = f'dict[_K, tuple[{return_tuple_types}]]'
    print(f"""\
@overload
def dict_zip_longest({arguments},
                     *,
                     fillvalue: Optional[_Fill] = None) -> {returns}: ...""")

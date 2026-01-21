from itertools import permutations
import functools

str_list = list(permutations("abcd", 4))
result_list = []

for string_set in str_list:
    this_string = functools.reduce(lambda a, b: a + b, string_set)
    result_list.append(this_string)

print(result_list)
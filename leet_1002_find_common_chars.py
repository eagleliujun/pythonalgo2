
def find_common_chars1(arr):

    total_dict = {}
    for item in arr:
        for i in range(len(item)):
            total_dict[item[i]] = 0

    arr_dict = []
    for i in range(len(arr)):
        arr_dict.append(total_dict.copy())

    for idx_string in range(len(arr)):
        for idx_char in range(len(arr[idx_string])):
            one_char = arr[idx_string][idx_char]
            if arr_dict[idx_string].get(one_char) >= 0:
                arr_dict[idx_string][one_char] += 1

    '''
    we should get something like this at this point
    [{'b': 1, 'e': 1, 'l': 2, 'a': 1, 'r': 0, 'o': 0}, 
     {'b': 1, 'e': 1, 'l': 2, 'a': 1, 'r': 0, 'o': 0}, 
     {'b': 0, 'e': 1, 'l': 2, 'a': 0, 'r': 2, 'o': 1}]
     
    '''
    # print(total_dict)

    for k, v in total_dict.items():
        small_v = arr_dict[0][k]
        is_zero = False
        for i in range(1, len(arr_dict)):
            if arr_dict[i][k] == 0:
                is_zero = True
                total_dict[k] = 0
                break
            else:
                if small_v > arr_dict[i][k]:
                    small_v = total_dict[k] = arr_dict[i][k]
                else:
                    total_dict[k] = small_v
        if is_zero:
            continue

    res = []
    for k, v in total_dict.items():
        for i in range(v):
            res.append(k)

    return res


def find_common_chars2(arr):
    pre_found = arr[0]

    for idx_str in range(1, len(arr)):
        new_found = ''
        for idx_char in range(len(pre_found)):
            if pre_found[idx_char] in arr[idx_str]:
                new_found += pre_found[idx_char]
                arr[idx_str] = arr[idx_str].replace(pre_found[idx_char], '', 1)
        pre_found = new_found
    return list(pre_found)


# awesome
def find_common_chars3(arr):
    if not arr:
        return []

    res = []
    for each in set(arr[0]):
        count = [w.count(each) for w in arr]
        s = each * min(count)
        # print("s", s)
        for i in s:
            res.append(i)

    return res


# super awesome
from functools import reduce
import collections
def find_common_chars4(arr):
    return list(reduce(collections.Counter.__and__, map(collections.Counter, arr)).elements())


arr1 = ['bella', 'label', 'roller']
arr2 = ['cool', 'lock', 'cook']

print(find_common_chars3(arr2))
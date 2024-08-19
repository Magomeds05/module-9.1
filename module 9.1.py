def apply_all_func(int_list, *functions):
    result =[]
    for i in functions:
        result.append(i)
    return result


print(apply_all_func([6, 20, 15, 9], max, min, len, sum, sorted))



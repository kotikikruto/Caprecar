from conversion import in_10, in_N  # Функции, переводящие число из n системы в 10ю и наоборот соответственно


def Make_values(k, b):
    list = []
    cur_len = 0
    cur_num = ''

    while int(k * str(b - 1)) not in list:
        i = 0
        while i < b:
            if (cur_len == 0 or int(cur_num[cur_len - 1]) <= i) and cur_len < k:
                cur_num += str(i)
                cur_len += 1
                print(cur_num, cur_len)
            else:
                i += 1
                cur_num = ''
                cur_len = 0

        list.append(int(cur_num))
        cur_num = ''
        cur_len = 0

    return list


print(Make_values(3, 2))

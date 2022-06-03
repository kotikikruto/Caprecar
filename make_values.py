from perevod import in_10, in_N  # Функции, переводящие число из n системы в 10ю и наоборот соответственно


def Make_values(l, s):
    list = []
    for j in range(s ** l // 2):
        n = in_N(j, s)
        c_1 = 0
        c_2 = 0
        c_3 = 0
        c_4 = 0
        c_5 = 0
        c_6 = 0
        c_7 = 0
        c_8 = 0
        c_9 = 0
        for i in range(len(n)):
            if n[i] == '1':
                c_1 += 1
            elif n[i] == '2':
                c_2 += 1
            elif n[i] == '3':
                c_3 += 1
            elif n[i] == '4':
                c_4 += 1
            elif n[i] == '5':
                c_5 += 1
            elif n[i] == '6':
                c_6 += 1
            elif n[i] == '7':
                c_7 += 1
            elif n[i] == '8':
                c_8 += 1
            elif n[i] == '9':
                c_9 += 1
        value = (
                        l - c_1 - c_2 - c_3 - c_4 - c_5 - c_6 - c_7 - c_8 - c_9) * '0' + c_1 * '1' + c_2 * '2' + c_3 * '3' + c_4 * '4' + c_5 * '5' + c_6 * '6' + c_7 * '7' + c_8 * '8' + c_9 * '9 '
        if value not in list:
            list.append(value)
    list_1 = []
    for i in range(len(list)):
        list_1.append(in_10(list[i], s))
    return list_1

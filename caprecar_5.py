# Капрекар для 5ной сс (вход и выход - в десятичной!)
from perevod import in_10, in_N


def Caprecar_5(n, l):
    n = in_N(n, 5)
    c_1 = 0
    c_2 = 0
    c_3 = 0
    c_4 = 0
    for i in range(len(n)):
        if n[i] == '1':
            c_1 += 1
        elif n[i] == '2':
            c_2 += 1
        elif n[i] == '3':
            c_3 += 1
        elif n[i] == '4':
            c_4 += 1

    capmax = c_4 * '4' + c_3 * '3' + c_2 * '2' + c_1 * '1' + (l - c_1 - c_2 - c_3 - c_4) * '0'
    capmin = (l - c_1 - c_2 - c_3 - c_4) * '0' + c_1 * '1' + c_2 * '2' + c_3 * '3' + c_4 * '4'

    return in_10(capmax, 5) - in_10(capmin, 5)

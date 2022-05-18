# Капрекар для 8ной сс (вход и выход - в десятичной!)
from perevod import in_10, in_N


def Caprecar_8(n, l):
    n = in_N(n, 8)
    c_1 = 0
    c_2 = 0
    c_3 = 0
    c_4 = 0
    c_5 = 0
    c_6 = 0
    c_7 = 0
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

    capmax = c_7 * '7' + c_6 * '6' + c_5 * '5' + c_4 * '4' + c_3 * '3' + c_2 * '2' + c_1 * '1' + (
            l - c_1 - c_2 - c_3 - c_4 - c_5 - c_6 - c_7) * '0'
    capmin = (
                     l - c_1 - c_2 - c_3 - c_4 - c_5 - c_6 - c_7) * '0' + c_1 * '1' + c_2 * '2' + c_3 * '3' + c_4 * '4' + c_5 * '5' + c_6 * '6' + c_7 * '7'

    return in_10(capmax, 8) - in_10(capmin, 8)

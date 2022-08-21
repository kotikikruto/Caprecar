# Капрекар для 3ной сс (вход и выход - в десятичной!)
from conversion import in_10, in_N


def Caprecar_3(n, l):
    n = in_N(n, 3)  # Перевела в троичную
    c_1 = 0
    c_2 = 0
    for i in range(len(n)):
        if n[i] == '1':
            c_1 += 1
        elif n[i] == '2':
            c_2 += 1

    capmax = c_2 * '2' + c_1 * '1' + (l - c_1 - c_2) * '0'
    capmin = (l - c_1 - c_2) * '0' + c_1 * '1' + c_2 * '2'

    return in_10(capmax, 3) - in_10(capmin, 3)

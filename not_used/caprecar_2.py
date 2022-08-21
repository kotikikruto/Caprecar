# Капрекар для двоичной сс (вход и выход - в десятичной!)
from conversion import in_10, in_N


def Caprecar_2(n, l):
    n = in_N(n, 2)  # Перевела в двоичную
    c_1 = 0
    for i in range(len(n)):
        if n[i] == '1':
            c_1 += 1

    capmax = c_1 * '1' + (l - c_1) * '0'
    capmin = (l - c_1) * '0' + c_1 * '1'

    return in_10(capmax, 2) - in_10(capmin, 2)

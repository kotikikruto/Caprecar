# Просто нечто бессмысленное (Выход - какие числа куда переходят)

from kaprekar import Kaprekar
from conversion import in_N


def F(n, sys):
    for i in range(sys ** n):
        s = ''
        for j in range(sys ** n):
            if Kaprekar(j, n, sys) == i:
                s += str(in_N(j, sys)) + ' '
        if len(s) != 0:
            print(s, "->", in_N(i, sys))


n = int(input("Введите длину числа: "))
s = int(input("Введите систему счисления: "))
F(n, s)

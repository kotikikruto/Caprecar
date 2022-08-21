# Соединяем отдельные функции капрекара в одну
from caprecar_10 import Caprecar_10
from caprecar_9 import Caprecar_9
from caprecar_8 import Caprecar_8
from caprecar_7 import Caprecar_7
from caprecar_6 import Caprecar_6
from caprecar_5 import Caprecar_5
from caprecar_4 import Caprecar_4
from caprecar_3 import Caprecar_3
from caprecar_2 import Caprecar_2


def Caprecar(n, l, s):
    if s == 10:
        return Caprecar_10(n, l)
    elif s == 9:
        return Caprecar_9(n, l)
    elif s == 8:
        return Caprecar_8(n, l)
    elif s == 7:
        return Caprecar_7(n, l)
    elif s == 6:
        return Caprecar_6(n, l)
    elif s == 5:
        return Caprecar_5(n, l)
    elif s == 4:
        return Caprecar_4(n, l)
    elif s == 3:
        return Caprecar_3(n, l)
    elif s == 2:
        return Caprecar_2(n, l)
    else:
        return "Error"
# Caprecar

Унары, либо унарные функции - это функция, которая принимает один аргумент.

Данная задача рассматривает конкретную функцию - функцию Капрекара.

Функция Капрекара принимает на вход число, записанное в s-ной системе счисления и имеющее длину l (Если длина числа меньше l, оно дополняется незначащими нулями)

Число разобьем на цифры, расположим цифры сначала в порядке возрастания, затем в порядке убывания. Вычтем из большего меньшее. Получим результат.

Например, для числа 241, длины l = 3 и системы счисления s = 10

Caprecar(241, 3, 10) = 421 - 124 = 297

Что необходимо узнать?

* Каковы неподвижные точки, циклы для функции при заданной длине и системе счисления?
* Каково максимальное число итераций, необходимое для того, чтобы любое число путем применения функции Капрекара приняло значение из цикла или неподвижной точки?

Например, для l = 4 и s = 10:

Две неподвижные точки - 0 и 6174.

Для того, чтобы достичь 6174 необходимо провести 7 итераций для любого числа, где все цифры неодинаковы.

Основная программа (main.py) решает данную задачу. Пока что она несовершенна, но с задачей тем не менее справляется.

``` python
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
    
```

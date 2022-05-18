# Основной файл
from caprecar import Caprecar
from search import Search_1, Search_2

lenght = int(input("Введите длину (от 2 до 10): "))  # Ввод длины числа
# system = 2
system = int(input("Введите систему счисления (от 2 до 10): "))  # Ввод системы счисления

range_of_values = list(range(system ** lenght // 2))  # Составляем область определения (Можно постараться уменьшить)
range_of_values_new = []  # Область значений функции капрекара, пока не заполнено

while True:
    for i in range(len(range_of_values)):
        c = Caprecar(range_of_values[i], lenght, system)
        if c not in range_of_values_new:
            range_of_values_new.append(c)  # Заполняем область значений
    if len(range_of_values) == len(range_of_values_new):
        break  # Из свойства унаров понятно, что в области значений не может появиться значение, которого
        # нет в области определения, тогда из равенства мощностей множеств следует равенство множеств

    range_of_values = range_of_values_new  # Теперь область значений стала областью определения
    range_of_values_new = []  # Новая область значений снова пустая

Search_1(range_of_values, lenght, system)  # Эта функция ищет циклы и неподвижные точки
Search_2(range_of_values, lenght, system)  # Эта функция ищет глубину дерева
# (максимальное число итераций, которое необходимо, чтобы войти в цикл или неподвижную точку)

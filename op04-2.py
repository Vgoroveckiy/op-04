# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью [кортежа](https://pythonworld.ru/tipy-dannyx-v-python/kortezhi-tuple.html), после return перечислить все значения через запятую): периметр квадрата, площадь квадрата и диагональ квадрата.

import math


def square(x):
    perimetr = x * 4
    ploshad = x * x
    diagonal = x * math.sqrt(2)
    return (perimetr, ploshad, diagonal)


print(square(5))

import math as m
def discriminant(a, b, c):
    if a != 0 and b != 0 and c != 0:
        d = pow(b, 2) - 4 * a * c
        if d > 0:
            x1 = (-b - m.sqrt(d)) / (2 * a)
            x2 = (-b + m.sqrt(d)) / (2 * a)
            x = (f"Корни данного уравнения: x1 = {x1}, x2 = {x2}")
        elif d == 0:
            x1 = -b/(2*a)
            x = (f"Данное уравнение имеет один корень: x = {x1}")
        else:
            x = ("Данное уравнение корней не имеет")

    elif a == 0:
        if b != 0:
            x1 = -c / b
            x = (f"Данное уравнение имеет один корень: x = {x1}")
        elif b == 0 and c == 0:
            x = ("Данное уравнение имеет бесконечное количество корней")

    return x


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

xa = int(input('Введите координату x точки a: '))
ya = int(input('Введите координату y точки a: '))
xb = int(input('Введите координату x точки b: '))
yb = int(input('Введите координату y точки b: '))
if xa > xb:
              x = xa - xb
else:
              x = xb - xa
if ya > yb:
              y = ya - yb
else:
              y = yb - ya
print('расстояние между точками А и В равно ', round(((y**2 + x**2)**0.5),2))
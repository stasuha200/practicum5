xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())
if (abs(x - xc) ** 2 + abs(y - yc) ** 2) ** (1 / 2) > r:
    print('Точка вне окружности')
elif (abs(x - xc) ** 2 + abs(y - yc) ** 2) ** (1 / 2) < r:
    print('Точка внутри окружности')
else:
    print('Точка на окружности')

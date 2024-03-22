weight = float(input())
height = float(input())
weight_kg = weight / 2.2046
height_m = height * 0.0254
imt = round(weight_kg / (height_m ** 2), 2)
if imt < 16:
    print('Выраженный дефицит массы тела')
elif 16 <= imt and imt <= 18.49:
    print("Недостаточная масса тела")
elif 18.5 <= imt and imt <= 24.99:
    print('Норма')
elif 25 <= imt and imt <= 29.99:
    print('Избыточная масса тела')
elif 30 <= imt and imt <= 34.99:
    print('Ожирение первой степени')
elif 35 <= imt and imt <= 39.99:
    print('Ожирение второй степени')
else:
    print('Ожирение третьей степени')

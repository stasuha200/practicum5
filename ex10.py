pincod = int(input())
a_1 = pincod // 1000
a_2 = pincod // 100 % 10
a_3 = pincod % 100 // 10
a_4 = pincod % 10
if ((a_1 >= 1) and (a_1 <= 9) and ((pincod < 1900) or (pincod > 2050))
        and (a_1 != a_2) and (a_1 != a_3) and (a_1 != a_4) and (a_2 != a_3)
        and (a_2 != a_4) and (a_3 != a_4)):
    print('OK')
else:
    print('ERROR')
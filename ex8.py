knat = int(input())
galleon = knat // (17 * 29)
sikl = (knat - (galleon * 17 * 29)) // 29
knat = knat - sikl * 29 - galleon * 17 * 29
if galleon == 0 and sikl == 0:
    print(f'{knat} кнатов')
elif galleon == 0 and knat == 0:
    print(f'{sikl} сиклей')
elif sikl == 0 and knat == 0:
    print(f'{galleon} галлеонов')
elif galleon == 0:
    print(f'{sikl} сиклей')
    print(f'{knat} кнатов')
elif sikl == 0:
    print(f'{galleon} галлеонов')
    print(f'{knat} кнатов')
elif knat == 0:
    print(f'{galleon} галлеонов')
    print(f'{sikl} сиклей')
else:
    print(f'{galleon} галлеонов')
    print(f'{sikl} сиклей')
    print(f'{knat} кнатов')

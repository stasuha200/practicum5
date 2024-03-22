counter = int(input())
if ((counter % 10 == counter // 1000) and (counter % 100 // 10 == counter // 100 % 10)
        and (counter // 1000 >= 1) and (counter // 1000 <= 9)):
    print('Настоящее')
else:
    print('Кривое')

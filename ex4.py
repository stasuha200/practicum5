parrots = int(input())
counter = parrots % 10
match counter:
    case 1:
        print(f'{parrots} попугай')
    case 2 | 3 | 4:
        print(f'{parrots} попугая')
    case 5 | 6 | 7 | 8 | 9 | 0:
        print(f'{parrots} попугаев')

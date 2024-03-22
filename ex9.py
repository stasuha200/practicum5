a = list(map(int, input().split()))
castle_1 = a[0]
castle_2 = a[1]
castle_3 = a[2]
castle = 0
if castle_1 < castle_2:
    castle = castle_1
    castle_1 = castle_2
    castle_2 = castle
    castle = 0
if castle_1 < castle_3:
    castle = castle_1
    castle_1 = castle_3
    castle_3 = castle
    castle = 0
if castle_2 < castle_3:
    castle = castle_2
    castle_2 = castle_3
    castle_3 = castle
    castle = 0
print(castle_1, castle_2, castle_3)

day_1 = int(input())
day_2 = int(input())
day_3 = int(input())
if day_1 == day_2 and day_2 == day_3:
    print(3)
elif day_1 == day_2 or day_2 == day_3 or day_1 == day_3:
    print(2)
else:
    print(1)

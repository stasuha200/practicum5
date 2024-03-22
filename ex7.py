a = list(map(int, input().split()))
n = a[0]
k = a[1]
m = a[2]
if m > k:
    print(m - k - 1)
elif m < k:
    print(n - k + (m - 1))
else:
    print(0)

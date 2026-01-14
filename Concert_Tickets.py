from bisect import bisect_right
n, m = map(int, input().split())
h = list(map(int, input().split()))
t = list(map(int, input().split()))
h.sort()
used = [0 for _ in range(n)]
for i in t:
    posi = bisect_right(h, i)
    fnd = 0
    if posi == n:
        posi -= 1
    for j in range(posi, -1, -1):
        if not used[j] and h[j] <= i:
            used[j] = 1
            fnd = 1
            print(h[j])
            break
    if not fnd:
        print(-1)
    
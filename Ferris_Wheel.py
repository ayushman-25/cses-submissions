n, x = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
ans = 0
i = 0
j = n - 1
while i <= j:
    if p[j] + p[i] > x:
        j -= 1
    else:
        i += 1
        j -= 1
    ans += 1
print(ans)
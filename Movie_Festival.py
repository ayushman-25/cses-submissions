n = int(input())
intervals = [list(map(int, input().split())) for _ in range(n)]
intervals.sort(key=lambda x: [x[1], x[0]])
end = 0
ans = 0
for [a, b] in intervals:
    if a >= end:
        ans += 1
        end = b
print(ans)

n = int(input())
events = list()
for _ in range(n):
    a, b = map(int, input().split())
    events.append([a, 1])
    events.append([b, -1])
events.sort()
ans = 0
cur = 0
for a, b in events:
    cur += b
    ans = max(ans, cur)
print(ans)
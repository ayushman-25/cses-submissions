from collections import defaultdict
n, sm = map(int, input().split())
arr = list(map(int, input().split()))
dd = defaultdict(list)
for i in range(n):
    dd[arr[i]].append(i + 1)
for i in arr:
    if dd[sm - i] and i != sm - i:
        print(dd[i][0], dd[sm - i][0])
        exit(0)
    if i == sm - i and len(dd[sm - i]) >= 2:
        print(dd[sm - i][0], dd[sm - i][1])
        exit(0)
print("IMPOSSIBLE")
n = int(input())
arr = list(map(int, input().split()))
if max(arr) < 0:
    print(max(arr))
    exit(0)
a = b = 0
for i in range(n):
    a = max(0, a + arr[i])
    b = max(b, a)
print(b)
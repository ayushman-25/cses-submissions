n, m, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
used = [0 for _ in range(n)]
cnt = 0
for i in b:
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) // 2
        if a[mid] < i - k:
            l = mid + 1
        elif a[mid] > i + k:
            r = mid - 1
        else:
            if used[mid]:
                l = mid + 1
            else:
                if mid > 0 and used[mid - 1]:
                    used[mid] = 1
                    cnt += 1
                    break
                if mid > 0 and not used[mid - 1] and not(i - k <= a[mid - 1] <= i + k):
                    used[mid] = 1
                    cnt += 1
                    break
                if mid == 0 or mid == n - 1:
                    used[mid] = 1
                    cnt += 1
                    break
                r = mid - 1
print(cnt)
    
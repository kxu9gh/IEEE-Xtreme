def compute(n, k, lst):
    if n <= k:
        return 0
    s = set(lst)
    if len(s) <= k:
        return 0
    s = sorted(list(s))
    i = 1
    diff = []
    while i < len(s):
        diff.append(s[i] - s[i-1])
        i += 1
    diff = sorted(diff)
    return max(diff[:n-k])

print(compute(5, 4, [30, 50, 41, 40, 20]))
import fileinput
def compute(n, k, lst):
    n = int(n)
    k = int(k)
    if n <= k:
        return 0
    s = set(lst)
    if len(s) <= k:
        return 0
    s = sorted(list(s))
    i = 1
    diff = []
    while i < len(s):
        diff.append(int(s[i]) - int(s[i-1]))
        i += 1
    diff = sorted(diff)
    return sum(diff[:len(s)-k])


stdin = []
for i in fileinput.input():
    stdin.append(i.rstrip())


line = 1
for testcase in range(int(stdin[0])):
    n, k = stdin[line].split()
    line += 1
    lst = stdin[line:line + int(n)]
    line += int(n)
    print(compute(n, k, lst))
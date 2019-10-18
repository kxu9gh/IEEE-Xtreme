import fileinput
def gcd(i, j):
    if i > j:
        return gcd(j, i)
    if j % i == 0:
        return i
    return gcd(j % i, i)


def Inti(n, a, b):
    sum = 0
    for i in range(a, b + 1):
        if gcd(i, n) == 1:
            sum += i
    return sum

stdin = []
for i in fileinput.input():
    stdin.append(i.rstrip())


line = 1
for testcase in range(int(stdin[0])):
    n, a, b = stdin[line].split()
    line += 1
    print(Inti(n, a, b))

# print(Inti(5, 1, 4))

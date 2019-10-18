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


print(Inti(5, 1, 4))

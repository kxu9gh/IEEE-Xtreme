# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


# numpy and scipy are available for use
import numpy
import scipy

n = get_number()
a = get_number()
b = get_number()


def compute(n, a, b):
    if n < a:
        print("NO")
        return None
    if 2 * a > n and b < n:
        print("NO")
        return None

    if b >= n:
        print("YES")
        print(n)
        return None

    l = n // b
    if n % b == 0:
        print("YES")
        for i in range(l):
            print(b, end=" ")
        return None
    ans = [b for i in range(l + 1)]
    r = (l + 1) * b - n

    p = 0
    while r > 0:
        if r <= b - a:
            ans[p] -= r
            break
        else:
            r -= b - a
            ans[p] = a
            p += 1
    print("YES")
    for t in ans:
        print(t, end=" ")


compute(n, a, b)
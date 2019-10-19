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

ans = []
def func():
    n = get_number()
    m = get_number()
    array = []
    plugin = []
    global ans
    for i in range(n):
        array.append(get_number())
    for i in range(m):
        plugin.append(get_number())

    plugin = sorted(plugin)
    j = 0
    largest = array[0] - 1
    for i in range(n):
        if array[i] <= largest:
            ans.append(array[i])
            continue
        largest = array[i]
        while j < len(plugin) and plugin[j] <= array[i]:
            ans.append(plugin[j])
            j = j + 1
        ans.append(array[i])
    if j < len(plugin):
        ans = ans + plugin[j:]

func()

for t in ans:
    print(t, end=" ")

def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)

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

a = get_number()
b = get_number()

def res(a,b):
    if a >= b:
        if a > 2 * b:
            return b
        else:
            x = ((a + b) // 3 + (a - b) + 1)//2
            y = ((a + b) // 3 - (a - b))//2
            return x + y
    else:
        return res(b,a)


result = res(a, b)

print(result)

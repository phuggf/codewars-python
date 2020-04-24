def zero(func = None):
    return num_func(func, 0)
def one(func = None):
    return num_func(func, 1)
def two(func = None):
    return num_func(func, 2)
def three(func = None):
    return num_func(func, 3)
def four(func = None):
    return num_func(func, 4)
def five(func = None):
    return num_func(func, 5)
def six(func = None):
    return num_func(func, 6)
def seven(func = None):
    return num_func(func, 7)
def eight(func = None):
    return num_func(func, 8)
def nine(func = None):
    return num_func(func, 9)

def num_func(func, num):
    if func == None: 
        return num
    else: 
        return int(func(num))

def plus(y):
    def plusFunc(x):
        return x + y
    return plusFunc
def minus(y):
    def minus_func(x):
        return x - y
    return minus_func
def times(y):
    def times_func(x):
        return x * y
    return times_func
def divided_by(y):
    def divided_func(x):
        return x / y
    return divided_func
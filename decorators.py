import functools

def print_result(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('Result is: ' + str(func(*args, **kwargs)))
    return inner

@print_result
def three_times(n):
    return n * 3

three_times(3)

##############################################################################

def check_type(input_type):
    def function_caller(func):
        @functools.wraps(func)
        def inner(n):
            if isinstance(n, input_type):
                return func(n)
            else:
                print('wrong type')
        return inner
    return function_caller

@check_type(int)
def three_times(n):
    return n * 3

print(three_times(3))

print(three_times('asd'))

##############################################################################


@check_type(int)
@print_result
def three_times(n):
    return n * 3

three_times(3)

three_times('asd')
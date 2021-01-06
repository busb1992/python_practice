# filtering from list
list_01 = [0, 1, 2, 3, 4, 5]

def filter_out_even_num(num):
    return num % 2 == 0

list(filter(filter_out_even_num, list_01))

# use map to create a new sequence

def get_square(num):
    return num ** 2

list(map(get_square, list_01))

# do the same with lambda
list(map(lambda num: num ** 2, list_01))
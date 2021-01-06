list_01 = [0, 1, 2, 3, 4, 5]
list_02 = [True, 'asd']

# any : if the values are TRUE
any(list_01)

# all : if all the values are TRUE
all(list_01)    # since 0 is False this return False
all(list_02)    # this is obvoiusly True

# min max sum
min(list_01)
max(list_01)
sum(list_01)
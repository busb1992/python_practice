# args
def test(*args):
    for arg in args:
        print(arg)

nums = [0,1,2,3,4]
test(*nums)
test(1,2,3,4)

# kwargs
def test2(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

test2(name="yasoob")

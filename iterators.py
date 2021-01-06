days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
activit_list = ['Bike', 'Hike', 'Bike', 'Hike', 'Bike']

# make it iterable
i = iter(days)
next(i)
next(i)
next(i)

# iteratrate oved days with index, wothout looping varaible
for index, day in enumerate(days, start=10):
    print(index, day)

# iterate over multiple lists
for day, activity in zip(days, activit_list):
    print('in ' + day + ' i will ' + activity)

############
# itertools
import itertools

# cycle
seq = ['N', 'E', 'S', 'W']
cycle_1 = itertools.cycle(seq)
next(cycle_1)
next(cycle_1)
next(cycle_1)
next(cycle_1)
next(cycle_1)

# counter
counter = itertools.count(23, 23)
next(counter)
next(counter)

# accomulator
vals = [10, 20, 30, 40, 50, 30]
acc = itertools.accumulate(vals)
list(acc)
acc = itertools.accumulate(vals, max)
list(acc)

# dropwhile takewhile

def test_func(num):
    return 40 > num

list(itertools.dropwhile(test_func, vals))
list(itertools.takewhile(test_func, vals))